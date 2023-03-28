# Написати функцію, яка повертає тільки однакові елементи двох множин.
set1 = {1, 2, 3, 4, 10, 69, 84, 7, 12}
set2 = {3, 7, 5, 6, 8, 10, 32, 69, 71}


def similar_units(set_1, set_2):
    lst1 = list(set_1)
    lst2 = list(set_2)
    similar_list = list()
    for item in lst1:
        for item_2 in lst2:
            if item == item_2:
                similar_list.append(item)
            else:
                continue
    similar_set = set(similar_list)
    return print(similar_set)


similar_units(set1, set2)



