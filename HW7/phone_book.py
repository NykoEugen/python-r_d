# Створити телефонну книгу, яка матиме наступні команди:
# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені

phone_book = []


def statistic():
    stats = len(phone_book)
    return print(f"The phone book contains with {stats} contacts")


def add_contact(first_name, last_name, phone_number):
    frst_name = first_name.capitalize()
    lst_name = last_name.capitalize()
    if not phone_number.isdigit():
        return print("Invalid number, only numeric")

    if len(phone_book) == 0:
        contact_info = {"name": frst_name,
                        "last_name": lst_name,
                        "phone_number": phone_number,
                        }
        phone_book.append(contact_info)
        return print(f"Contact {contact_info.get('name')} add successful")

    if len(phone_book) > 0:
        for i in phone_book:
            if i.get('name') == frst_name and i.get('last_name') == lst_name:
                return print(f"Contact {frst_name} {lst_name}  does exist in phone book")

        contact_info = {"name": frst_name,
                        "last_name": lst_name,
                        "phone_number": phone_number,
                        }
        phone_book.append(contact_info)
        return print(f"Contact {contact_info.get('name')} add successful")


def delete_contact(first_name, last_name):
    frst_name = first_name.capitalize()
    lst_name = last_name.capitalize()
    deleted_contact = ''
    for i in phone_book:
        if frst_name == i.get("name") and lst_name == i.get("last_name"):
            deleted_contact = frst_name
            phone_book.remove(i)
            return print(f"Contact {frst_name} {lst_name} was deleted successful")
    if deleted_contact != frst_name:
        return print(f"Contact {frst_name} {lst_name} doesn't exist")


def lst_contact():
    lst_contacts = []
    if len(phone_book) == 0:
        return print("The phone book is empty")
    else:
        for i in phone_book:
            full_name = i.get("name") + " " + i.get("last_name")
            lst_contacts.append(full_name)
    return print(lst_contacts)


def show_contact(first_name, last_name):
    frst_name = first_name.capitalize()
    lst_name = last_name.capitalize()
    showing_contact = ''
    for i in phone_book:
        if frst_name == i.get("name") and lst_name == i.get("last_name"):
            showing_contact = frst_name
            return print(f"Name: {i.get('name')}.\nLast name: {i.get('last_name')}.\nPhone number: {i.get('phone_number')}.")
    if showing_contact != frst_name:
        return print(f"Contact {frst_name} {lst_name} doesn't exist")


def main():
    print("Phone book has next command: stats, list, add , delete , show , close")
    in_request = input("Print your command: ").lower()
    if in_request == "stats":
        statistic()

    if in_request == "add":
        in_request = input("Print: Name, Last name, Phone number: ")
        full_info = list(in_request.split(", "))
        add_contact(full_info[0], full_info[1], full_info[2])

    if in_request == "delete":
        in_request = input("Print: Name Last name: ")
        dell_info = list(in_request.split(" "))
        delete_contact(dell_info[0], dell_info[1])

    if in_request == "list":
        lst_contact()

    if in_request == "show":
        in_request = input("Print: Name Last name: ")
        show_info = list(in_request.split(" "))
        show_contact(show_info[0], show_info[1])

    if in_request == "close":
        exit()


if __name__ == "__main__":
    while True:
        main()

