# def annual_credit(credit_amount, years, percentage=0.1):
#     total_credit_amount = credit_amount * (1 + percentage * years)
#     return total_credit_amount

def credit():
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
