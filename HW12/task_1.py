# Написати власний декоратор, задачею якого має бути друк назви функції і часу,
# коли вона була викликана. Декоратор має працювати для різних функцій однаково.
import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Name of func {func.__name__}")
        print(f"Start at {time.strftime('%X', time.localtime())}")
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def biggest_arg(*args):
    biggest_argument = 0
    for i in args:
        if i > biggest_argument:
            biggest_argument = i
            continue
    return biggest_argument


num = biggest_arg(10, 25, 1, 15, 35, 158, 21, 2, 68 )
print(num)


@my_decorator
def my_func(a, b, name=None, year=None):
    print(a, b, name, year)


my_func(1, 2, name="Eugen", year=1995)
