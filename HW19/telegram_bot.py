from HW19.Bot import Bot


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")


some_bot = TelegramBot("Alex")
# some_bot.send_message("Hello")
some_bot.say_name()

some_bot.set_url("bot.com")
some_bot.set_chat_id(1)
some_bot.send_message("Hello")
