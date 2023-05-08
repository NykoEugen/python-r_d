class User:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        if self.name == other:
            return True
        else:
            return False


user1 = User("Alex")
user2 = User("ALEX")
print(user1 == user2)
