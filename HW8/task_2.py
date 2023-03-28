# Написати функцію, яка повертає тільки унікальні елементи двох множин.
set1 = {1, 2, 3, 4, 10, 69, 84, 7, 12}
set2 = {3, 7, 5, 6, 8, 10, 84, 69, 71}


def unique_unit(set_1, set_2):
    union_lst = list(set_1) + list(set_2)
    unique_list = list()

    for item in union_lst:
        if union_lst.count(item) < 2:
            unique_list.append(item)

    unique_set = set(unique_list)
    return print(unique_set)


unique_unit(set1, set2)