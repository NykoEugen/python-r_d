# Перетворити всі елементи списку типу string в верхній регістр, використовуючи map
lst = ['Gygdfe', 'dfeeRFed', 'H32bnJ', 'hsbnje', 'HBuuuw Jfds']


def upper_case(item):
    return item.upper()


upper_lst = list(map(upper_case, lst))
print(upper_lst)