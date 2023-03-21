# Створити функцію, яка сумує будь-яку кількість аргументів і повертає результат.
def summary_args(*args):
    amount = 0
    for i in args:
        amount += i
    return amount

print(summary_args(15,5,80,25))
