# =====================================================================
# simple method done exception, but long for discovered)

class MyManeger:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Program incomplete, error: {exc_val}")
            print("=" * 10)
            return True
        print("=" * 10)


def biggest_arg(*args):
    biggest_argument = 0
    for i in args:
        if i > biggest_argument:
            biggest_argument = i
            continue
    return biggest_argument


with MyManeger():
    values = (10, 15.8, 1, 15, 35, 158, 21, 2, 68)
    print(biggest_arg(*values))


# =====================================================================
# first prototype of solution this task, but not so flexible

# class MyManeger:
#     def __init__(self, func, *args):
#         self.func = func
#         self.args = args
#
#     def __enter__(self):
#         print("=" * 10)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is not None:
#             print(f"Program incomplete, error: {exc_val}")
#         print("=" * 10)
#
#     def run(self):
#         try:
#             result = self.func(*self.args)
#             print(f"Result is: {result}")
#         except Exception as e:
#             print(f"Program incomplete: {e}")
#
#
# def biggest_arg(*args):
#     biggest_argument = 0
#     for i in args:
#         if i > biggest_argument:
#             biggest_argument = i
#             continue
#     return biggest_argument
#
#
# values = (10, "fwse", 1, 15, 35, 158, 21, 2, 68)
# with MyManeger(biggest_arg, *values) as n:
#     n.run()

# =====================================================================
# second prototype of solution this task, not so flexible

# class MyManeger:
#     def __init__(self, func, *args):
#         self.func = func
#         self.args = args
#
#     def __enter__(self):
#         print("=" * 10)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             result = self.func(*self.args)
#             print(f"Result is: {result}")
#         except Exception as e:
#             print(f"Program incomplete: {e}")
#         if exc_type is not None:
#             print(f"Program incomplete, error: {exc_val}")
#         print("=" * 10)
#
#
# def biggest_arg(*args):
#     biggest_argument = 0
#     for i in args:
#         if i > biggest_argument:
#             biggest_argument = i
#             continue
#     return biggest_argument
#
#
# values = (10, 1, 15, 35, 158, 21, 2, 68)
# with MyManeger(biggest_arg, *values) as n:
#     n
