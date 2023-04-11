# Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.

def print_number(n):
    if n == 0:
        print("0")
        return
    print(n, end=", ")
    return print_number(n - 1)


print_number(10)
