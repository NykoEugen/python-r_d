# Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(8))