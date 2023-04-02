# Написати функцію, яка повертає тільки унікальні елементи двох множин.
set1 = {1, 2, 3, 4, 10, 69, 84, 7, 12}
set2 = {3, 7, 5, 6, 8, 10, 84, 69, 71}


def unique_unit(set_1, set_2):
    unique_set1 = set_1.difference(set_2)
    unique_set2 = set_2.difference(set_1)
    unique_set = unique_set1.union(unique_set2)
    return unique_set


print(unique_unit(set1, set2))