from credit_calculator import credit
from documents import enter_result
from documents import create_template
from documents import edit_template
from telebot import run_bot

def main_menu():
    create_template()
    
    while True:
        print("===== Головне меню ============")
        print("1 - Кредит")
        print("2 - Ввести данні")
        print("3 - Запустити телеграм бот")
        print("4 - Редагувати шаблон")
        print("5 - Вихід")
        
        user_choice = input("Виберіть функцію: ")
        
        if user_choice  == "1":
            credit()
        elif user_choice  == "2":
            enter_result()
        elif user_choice  == "3":
            run_bot()
        elif user_choice  == "4":
            edit_template()
        elif user_choice == "5":
            print("Вихід з програми...")
            break
        else:
            print("Спробуйте ще раз.")

main_menu()
