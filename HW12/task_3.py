# Переписати декоратор із першого завдання, щоб він приймав
# цілочисельний аргумент `times`. Стільки разів виконувавати
# друк назви функції і часу, скільки ‘times’ задано.
import time


def my_decorator(times):
    def wrapper(func):
        def inner(*args, **kwargs):
            for i in range(1, times + 1):
                print(f"Name of func {func.__name__}")
                print(f"Start at {time.strftime('%X', time.localtime())}")
            return func(*args, **kwargs)
        return inner
    return wrapper


@my_decorator(3)
def biggest_arg(*args):
    biggest_argument = 0
    for i in args:
        if i > biggest_argument:
            biggest_argument = i
            continue
    return biggest_argument


num = biggest_arg(10, 25, 1, 15, 35, 158, 21, 2, 68 )
print(num)


@my_decorator(2)
def my_func(a, b, name=None, year=None):
    print(a, b, name, year)


my_func(1, 2, name="Eugen", year=1995)