# Написати функцію, яка повертає тільки однакові елементи двох множин.
set1 = {1, 2, 3, 4, 10, 69, 84, 7, 12}
set2 = {3, 7, 5, 6, 8, 10, 32, 69, 71}


def similar_units(set_1, set_2):
    similar_units = set_1.intersection(set_2)
    return similar_units


print(similar_units(set1, set2))



