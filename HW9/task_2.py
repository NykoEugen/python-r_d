# Створити програму, яка буде приймати число і друкувати відповідне
# число в послідовності Фібоначчі, використовуючи рекурсію


def fibo_number(i):
    if i <= 1:
        return i
    else:
        return fibo_number(i - 1) + fibo_number(i - 2)


print(fibo_number(6))

