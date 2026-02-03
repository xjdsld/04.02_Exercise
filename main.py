from datetime import date
import telebot
import sqlite3

def annual_credit(credit_amount, years, percentage=0.1):
    total_credit_amount = credit_amount * (1 + percentage * years)
    return total_credit_amount

def data_enter():
    today = date.today()
    data = {
        "pib": input('ПІБ отримувача: '),
        "pass": input('Серія та номер паспорту: '),
        "dano": input('ПІБ, ким видано: '),
        "date": today,
        "ps": input('Підпис: __________: ')
    }
    return data


def enter_result():
    data = data_enter()
    with open("template.txt", encoding="utf-8") as f:
        template = f.read()
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(template.format(**data))

def credit_console():
    while True:
        print("\n" + "="*30)
        try:
            amount_str = input("1. Сума кредиту (грн) [або 'exit']: ")
            if amount_str.lower() == 'exit':
                break

            amount = float(amount_str)
            years = int(input("2. Термін (років): "))
            rate_input = input("3. Річна ставка % (натисніть Enter для 10%): ")

            if rate_input.strip() == "":
                rate = 10.0
            else:
                rate = float(rate_input)

            overpayment = amount * (rate / 100) * years
            total_sum = amount + overpayment
            months = years * 12
            monthly_payment = total_sum / months

            print("\n--- РОЗРАХУНОК ДЛЯ КЛІЄНТА ---")
            print(f"Сума на руки:      {amount:,.2f} грн")
            print(f"Відсоткова ставка: {rate}%")
            print(f"Термін:            {years} років ({months} міс.)")
            print("-" * 30)
            print(f"ЩОМІСЯЧНИЙ ПЛАТІЖ: {monthly_payment:,.2f} грн")
            print(f"Переплата банку:   {overpayment:,.2f} грн")
            print(f"ВСЬОГО ДО СПЛАТИ:  {total_sum:,.2f} грн")
            print("==============================\n")

        except ValueError:
            print("\n[Помилка] Будь ласка, вводьте тільки цифри.")

def create_template():
    with open("template.txt", "w", encoding="utf-8") as f:
        f.write(
            "\nПІБ отримувача:\n"
            "Серія та номер паспорту:\n"
            "ПІБ, ким видано:\n"
            "Дата:\n"
            "Підпис: __________\n"
        )

def edit_template():
    with open("result.txt", "r", encoding="utf-8") as f:
        text_file = f.read()
        print(text_file)

    user = input('Edit template? Yes/no: ').strip().lower()
    if user == 'yes':
        print("~Enter new rows, click 'OK', if want to exit~\n")
        lines = []
        while True:
            row = input(': ')
            if row.lower() == 'ok':
                break
            lines.append(row)

        with open("template.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

bot = telebot.TeleBot("") 
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {}
    bot.send_message(message.chat.id, "Введіть ПІБ отримувача:")
    bot.register_next_step_handler(message, get_pib)

def get_pib(message):
    user_data[message.chat.id]["pib"] = message.text
    bot.send_message(message.chat.id, "Серія та номер паспорту:")
    bot.register_next_step_handler(message, get_passport)

def get_passport(message):
    user_data[message.chat.id]["passport"] = message.text
    bot.send_message(message.chat.id, "ПІБ, ким видано:")
    bot.register_next_step_handler(message, get_dano)

def get_dano(message):
    user_data[message.chat.id]["dano"] = message.text
    bot.send_message(message.chat.id, "Підпис:")
    bot.register_next_step_handler(message, get_ps)

def get_ps(message):
    data = user_data[message.chat.id]
    data["ps"] = message.text
    data["date"] = date.today()
    with open("template.txt", encoding="utf-8") as f:
        template = f.read()
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(template.format(**data))
    bot.send_message(message.chat.id, "Документ створено ✅")

def save_user(agreement_number, PIB_client, total):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        agreement_number INTEGER, 
        PIB_client TEXT, 
        total REAL
    )""")
    cursor.execute(
        "INSERT INTO users (agreement_number, PIB_client, total) VALUES (?, ?, ?)",
        (agreement_number, PIB_client, total)
    )
    connection.commit()
    connection.close()


def main_menu():
    create_template()
    
    while True:
        print("\n===== Головне меню =====")
        print("1 - Credit Console")
        print("2 - Enter data manually")
        print("3 - Run Telegram Bot")
        print("4 - Exit")
        
        mode = input("Виберіть режим: ").strip()
        
        if mode == "1":
            credit_console()
        elif mode == "2":
            enter_result()
        elif mode == "3":
            bot.polling()
        elif mode == "4":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main_menu()

