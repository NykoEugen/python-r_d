# Вивести всі елементу масиву, які є числом, використовуючи filter.
lst = ['fbu32bnj', '32', "23", '34nj']


def is_num(item):
    if item.isdigit():
        return item
    else:
        return False


result = list(filter(is_num, lst))
print(result)
