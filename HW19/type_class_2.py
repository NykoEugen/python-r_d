Bot = type("Bot", (), {'__init__': lambda self, name: setattr(self, 'name', name),
                       'say_name': lambda self: print(getattr(self, 'name')),
                       'send_message': lambda self, message: print(message)})


TelegramBot = type("TelegramBot", (Bot, ), {
    '__init__': lambda self, name, url=None, chat_id=None: Bot.__init__(self, name),
    'set_url': lambda self, url: setattr(self, 'url', url),
    'set_chat_id': lambda self, chat_id: setattr(self, 'chat_id', chat_id),
    'send_message': lambda self, message: print(f"{getattr(self, 'name')} bot say {message} "
                                                f"to chat {getattr(self, 'chat_id')} using {getattr(self, 'url')}")


})


bot = Bot('Fox')
bot.say_name()
bot.send_message('Test text')

bot2 = TelegramBot('Alex')
bot2.say_name()
bot2.set_url('test.com')
bot2.set_chat_id(2)
print(bot2.url)
print(bot2.chat_id)
bot2.send_message('Test text')

