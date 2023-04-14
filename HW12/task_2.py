# Написати власний менеджер контексту, задачею якого буде
# друкувати "==========" – 10 знаків дорівнює перед виконанням
# коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована
# текстом, проте програма не має завершити своєї роботи.


class MyManeger:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("=" * 10)


def biggest_arg(*args):
    biggest_argument = 0
    for i in args:
        if i > biggest_argument:
            biggest_argument = i
            continue
    return biggest_argument


with MyManeger():
    try:
        print(biggest_arg(10, 'fwe', 1, 15, 35, 158, 21, 2, 68))
    except Exception as e:
        print(f"Program incomplete, checkout error: {e}")

