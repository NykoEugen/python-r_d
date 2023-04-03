# Вивести всі елементу масиву, які є числом, використовуючи filter.
lst = ['fbu32bnj', '32', 25, 25.3, 51848421, "23", '34nj']


def is_num(item):
    if type(item) == str:
        if item.isdigit():
            return True
    if type(item) == int or type(item) == float:
        return True


result = list(filter(is_num, lst))
print(result)
