import re

file_name = input("Insert file name: ")
with open(file_name, 'r') as file:
    text = file.read()


# Replace email address for *@*
def email_replacer(text):
    pattern = r'\b[\w.-]+@[\w+]+\.[\w]{2,}\b'
    replaced_email = re.sub(pattern, '*@*', text)
    return replaced_email


# Replace email address for X***@****X
def defragment_text(text):
    pattern = r'(\b\w)(\w*)(\w{0,1})@(\w*)(\w{0,1})(\.\w{2,3}\b)'
    new_text = re.sub(pattern, replace_email, text)
    return new_text


def replace_email(match):
    modify_text = match.group(1) + '*' * len(match.group(2)) + match.group(3)\
                  + '@' + '*' * len(match.group(4)) + match.group(5) + match.group(6)[-1]
    return modify_text


modify_text = email_replacer(text)
print(modify_text)
print(defragment_text(text))


