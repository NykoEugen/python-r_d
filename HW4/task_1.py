sample_text = input("Input some text or args: ")
st_list = list(sample_text)

is_num = False
is_char = False

for i in st_list:
    if i.isdigit():
        is_num = True
    elif i.isalpha():
        is_num = False
        is_char = True

if is_num == True and is_char == False:
    print("It's number")
    input_number = float(sample_text)
    if input_number % 2:
        print("This number is ODD")
    else:
        print("This number is EVEN")
else:
    print("It's string")
    str_length = len(sample_text)
    print(f"This string is {str_length} length chars")
