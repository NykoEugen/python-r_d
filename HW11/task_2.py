class MyCustomException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def get_error_code(self):
        return self.error_code


try:
    raise MyCustomException("Error", 42)
except MyCustomException as exc:
    print(f"My exception {exc.get_error_code()}: {exc}")