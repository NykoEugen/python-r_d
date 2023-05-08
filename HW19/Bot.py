class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"{self.name}")

    def send_message(self, message):
        print(f"{message}")


# bot = Bot("Alex")
# bot.say_name()
# bot.send_message("This is message!")
