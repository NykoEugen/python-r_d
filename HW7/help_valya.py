tel_list = [{"Name": "Tom", "Surname": "Hardy", "Phone number": "+49 1626 345 74 63"},
            {"Name": "Megan", "Surname": "Fox", "Phone number": "+49 7685 737 78 37"},
            {"Name": "Amanda", "Surname": "Seyfried", "Phone number": "+49 8766 367 74 63"},
            {"Name": "Adam", "Surname": "Sandler", "Phone number": "+49 5658 756 74 66"}]

import json
#===============================================================
# Цей блок коду помістити в окрему функцію, наприклад ініціалізація.
# Кожен раз він буде робити перевірку на існування файлу та його загрузку.
# У майбутньому її треба буде переробити, щоб вона була універсальна,
# приймала аргументи і працювала з разними файлами, наприклад логами


def initialization():  #def initialization(file_name, log_file):
    try:
        with open("tele_data.txt", "x") as f:       # я створила файл спочатку, загрузила дані. це працює один раз спочатку
            json.dump(tel_list, f)
    except FileExistsError:
        print("File already exists!")

    try:
        with open("tele_data.txt", "r") as file:  # відкрила файл для читання і роботи з даними, це працює після запуску
            data = file.read()
            tele_data = json.loads(data)
            print(type(tele_data))
            print(tele_data)
            return tele_data
    except:
        print("Problem opening file!")


tele_data = initialization()
#==========================================================
# def phone_book(tele_data):


def stats():
    contacts_stats = len(tele_data)
    return print(f"In the phone book {contacts_stats} contacts")


def add_contact():
    f = {}
    f["Name"] = input("Enter contact name:  ")
    f["Surname"] = input("Enter contact surname: ")
    while True:
        try:
            f["Phone number"] = int(input("Enter contact phone number: "))
            break
        except ValueError:
            print("You didn't enter a number")
    tele_data.append(f)
    # load_data(tele_data) додати в майбутньому
    return print("Contact added")
    # print(tele_data)


def delete_contact():
    delete_list = {"Surname": "  "}
    delete_list["Surname"] = input("To delete contact enter surname: ")

    while True:
        try:
            search_contact = False
            for contact in tele_data:
                if contact['Surname'] == delete_list['Surname']:
                    search_contact = True
                    tele_data.remove(contact)
                    #load_data(tele_data, file_name) щось типу такого, але я б порадив подумати і про сам файл як аргумент.
                    print(f"Contact {contact['Name']} {contact['Surname']} delete")
                    break
            if not search_contact:
                raise ValueError("Surname not found")
            break
        except KeyError:
            print("Contact deletion error")
        except ValueError as e:
            print(e)
            break
#=====================================================================
# Ось цю частину коду треба виконувати після кожного додавання або видалення контакту,
# тому треба зробити з нього окрему функцію, яку ти будеш використовувати, з середени
# функцій додавання або видалення, але тут треба доробити функцію, щоб вона приймала аргументи і була
# універсальною
def load_data(tele_data): # def load_data(tele_data, file_name)
    try:
        #with open(file_name, "w") це для прикладу, але думаю зрозуміло
        with open("tele_data.txt", "w") as file:  # перезаписала дані після додавання та видалення контактів, працює після змін
            json.dump(tele_data, file)
            print(type(tele_data))
    except:
        print("Problem opening file!")
#======================================================================


def lst_contact():
    if input("Display a list of contacts?") == "yes":
        for contact in tele_data:
            for key, value in contact.items():
                if key == "Surname":
                    print(value)


def show_contact():
    search = input("Enter surname to search: ")
    for contact in tele_data:
        for key, value in contact.items():
            if value == search:
                print(json.dumps(contact, indent=2, separators=(",", ": ")).replace("{", "").replace("}", ""))# щось дуже складне)

    return f"Number of contacts after changes: {len(tele_data)}"


while True:
    in_request = input("Print your command: ").lower().replace(" ", "")
    if in_request == "stats":
        stats()

    if in_request == "add":
        add_contact()

    if in_request == "exit":
        exit()

# далі по анології вже придумаєш свої команди. Але не забувай про різні перевірки.
# Впринципі весь твій код залишився, я нічого не міняв, а лише розбив його на функції.
# Показав як повинна виглядати програма, тепер вона легко маштабується, є різні команди,
# можеш прикрутити різні декоратори, виконується до поки не буде введена команда exit. Думаю в
# тебе все вийде, логіка програми добра.