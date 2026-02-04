import telebot
from datetime import date

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


def run_bot():
    bot.polling()
