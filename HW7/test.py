import json
from json import JSONDecodeError

phone_book = []
contact_info = {"name": "frst_name8",
                "last_name": "lst_name8",
                "phone_number": "phone_number8"
                }
# phone_book.append(contact_info)

# with open("contact.json", "w") as file:
#     json.dump(phone_book, file)
#
# with open("contact.json", "r") as file:
#     json_data = file.read()
#     print(type(json_data))
#
# phone_book = json.loads(json_data) # list
# print(type(phone_book))
# print(phone_book)
# new_contact = {"name": "frst_name1",
#                "last_name": "lst_name1",
#                "phone_number": "phone_number1"
#               }
#
# phone_book.append(new_contact)
# new_json_data = json.dumps(phone_book)
# print(type(new_json_data))
#
# with open("contact.json", "w") as file:
#     file.write(new_json_data)

file_name = "contact.json"
def rewrite_json(file_name, new_data):
    with open(file_name, "r") as file:
        try:
            json_data = file.read()
            print(json_data)
            print(type(json_data))
            data = json.loads(json_data)
            print(data)
            print(type(data))
        except JSONDecodeError:
            data = []

    data.append(new_data)

    new_json_data = json.dumps(data)
    print(new_json_data)
    print(type(new_json_data))
    with open(file_name, "w") as file:
        file.write(new_json_data)

rewrite_json(file_name, contact_info)


