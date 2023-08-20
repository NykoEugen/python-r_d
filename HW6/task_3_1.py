# Знайти найбільший елемент масиву
# — створити свою функцію

def biggest_arg(*args):
    biggest_argument = float('-inf')
    for i in args:
        if i > biggest_argument:
            biggest_argument = i
            continue
    return biggest_argument


# print(biggest_arg(10, 25, 1, 15, 35, 158, 21, 2, 68))
