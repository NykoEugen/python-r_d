def init(self, name):
    self.name = name


def say_name(self):
    print(f"{self.name}")


def send_message(self, message):
    print(message)


Bot = type("Bot", (), {'__init__': init,
                       'say_name': say_name,
                       'send_message': send_message})


def init2(self, name, url=None, chat_id=None):
    self.name = name
    self.url = url
    self.chat_id = chat_id


def set_url(self, url):
    self.url = url


def set_chat_id(self, chat_id):
    self.chat_id = chat_id


def send_message(self, message):
    print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")


TelegramBot = type("TelegramBot", (Bot, ), {"__init__": init2,
                                            "set_url": set_url,
                                            "set_chat_id": set_chat_id,
                                            "send_message": send_message})

bot2 = TelegramBot("FOX")
bot2.say_name()
bot2.set_url("bot.com")
bot2.set_chat_id(2)
bot2.send_message("Text")

bot1 = Bot("Alex")
bot1.say_name()
bot1.send_message("Test")
