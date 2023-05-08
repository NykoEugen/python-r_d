class MyStr(str):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        upper_text = self.text.upper()
        return upper_text


my_str = MyStr("test text")
print(my_str)
