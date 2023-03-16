# Створити програму, яка буде друкувати в консоль “I love Python”
# кожні 4.2 секунди, поки її виконання не буде перервано вручну.

import time
while True:
    print(f"I love Python")
    time.sleep(4.2)