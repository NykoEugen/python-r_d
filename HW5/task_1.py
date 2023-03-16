# Створити програму, яка буде очікувати від користувача введення
# тексту і виведе інформацію по кожному надрукованому символу:
#
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”
sample_text = input("Input some text: ")
st_list = list(sample_text)

for symbol in st_list:
    if symbol.isalpha():
        if symbol.islower():
            print(f"The symbol {symbol} is letter and lower case")
            continue
        else:
            print(f"The symbol {symbol} is letter and upper case")
            continue

    if symbol.isdigit():
        if int(symbol) % 2:
            print(f"The symbol {symbol} is digit and ODD")
            continue
        else:
            print(f"The symbol {symbol} is digit and EVEN")
            continue

    else:
        print(f"This '{symbol}' is symbol")
