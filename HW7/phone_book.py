import json
import os
import time
from json import JSONDecodeError


# Initial all log files (phone book, log file, log error). Checkup log files.
def initialized_json(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            file.write('[]')

    with open(file_name, "r") as file:
        try:
            json_data = file.read()
            lst = json.loads(json_data)
            return lst
        except JSONDecodeError:
            lst = []
            return lst


phone_book = initialized_json("phone_book.json")
log_error = initialized_json("log_error.json")
log_file = initialized_json("log_file.json")
# print(phone_book)
# print(log_error)
# print(log_file)


# Decorator which loging name of func and time when the func was called
def name_time_decorator(func):
    def wrapper(*args, **kwargs):
        name_func = func.__name__
        time_call = time.strftime('%X', time.localtime())

        new_data = {
                        "name": name_func,
                        "time": time_call,
                   }
        rewrite_json("log_file.json", new_data)
        return func(*args, **kwargs)
    return wrapper


# Func which rewrite all changes in program.
def rewrite_json(file_name, new_data, delete=False):
    with open(file_name, "r") as file:
        try:
            json_data = file.read()
            data = json.loads(json_data)
        except JSONDecodeError:
            data = []

    data.append(new_data)

    new_json_data = json.dumps(data)
    with open(file_name, "w") as file:
        file.write(new_json_data)

    if delete:
        new_json_data = json.dumps(new_data)
        with open("phone_book.json", "w") as file:
            file.write(new_json_data)


# Simple func for processing exception errors and log it
def data_error(err):
    error_time = time.strftime('%X', time.localtime())
    error = str(err)
    data_error = {"error": error, "time": error_time}
    return data_error


@name_time_decorator
def statistic():
    stats = len(phone_book)
    return print(f"The phone book contains with {stats} contacts")


@name_time_decorator
def add_contact(first_name, last_name, phone_number):
    frst_name = first_name.capitalize()
    lst_name = last_name.capitalize()
    try:
        int(phone_number)
    except ValueError as e:
        data = data_error(e)
        rewrite_json("log_error.json", data)
        return print(f"Phone number should contain only numeric")

    if len(phone_book) == 0:
        contact_info = {"name": frst_name,
                        "last_name": lst_name,
                        "phone_number": phone_number,
                        }
        phone_book.append(contact_info)
        rewrite_json("phone_book.json", contact_info)
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
        rewrite_json("phone_book.json", contact_info)
        return print(f"Contact {contact_info.get('name')} add successful")


@name_time_decorator
def delete_contact(first_name, last_name):
    frst_name = first_name.capitalize()
    lst_name = last_name.capitalize()
    deleted_contact = ''
    for i in phone_book:
        if frst_name == i.get("name") and lst_name == i.get("last_name"):
            deleted_contact = frst_name
            phone_book.remove(i)
            rewrite_json("phone_book.json", phone_book, delete=True)
            return print(f"Contact {frst_name} {lst_name} was deleted successful")
    if deleted_contact != frst_name:
        return print(f"Contact {frst_name} {lst_name} doesn't exist")


@name_time_decorator
def lst_contact():
    lst_contacts = []
    if len(phone_book) == 0:
        return print("The phone book is empty")
    else:
        for i in phone_book:
            full_name = i.get("name") + " " + i.get("last_name")
            lst_contacts.append(full_name)
    return print(lst_contacts)


@name_time_decorator
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


def check_request(command, request_str):
    request = request_str.replace(" ", "")
    info = list(request.split(","))
    try:
        if command == "add":
            add_contact(info[0], info[1], info[2])
        if command == "delete":
            delete_contact(info[0], info[1])
        if command == "show":
            show_contact(info[0], info[1])
    except IndexError as e:
        data = data_error(e)
        rewrite_json("log_error.json", data)
        return print("Some argument doesn't fill")


def main():
    print("=======================================================================")
    print("Phone book has next command: stats, list, add , delete , show , close")
    in_request = input("Print your command: ").lower().replace(" ", "")
    if in_request == "stats":
        statistic()

    if in_request == "add":
        in_request = input("Print, data format: Name, last name, phone number: ")
        check_request("add", in_request)

    if in_request == "delete":
        in_request = input("Print, data format: First name, last name: ")
        check_request("delete", in_request)

    if in_request == "list":
        lst_contact()

    if in_request == "show":
        in_request = input("Print, data format: First name, last name: ")
        check_request("show", in_request)

    if in_request == "close":
        print("Phone book is closing")
        exit()


if __name__ == "__main__":
    while True:
        main()

