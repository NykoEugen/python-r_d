# Створити програму, яка буде приймати число і друкувати відповідне
# число в послідовності Фібоначчі, використовуючи рекурсію


def fibo_number(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        next_number = fibo_number(i - 1) + fibo_number(i - 2)
        return next_number


def fibo_sequence(n):
    sequence = []
    for i in range(n+1):
        sequence.append(fibo_number(i))
    return sequence


m = 10
n = fibo_sequence(m)
print(n)

print(fibo_number(m))
