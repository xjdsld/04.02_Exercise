from datetime import date

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
