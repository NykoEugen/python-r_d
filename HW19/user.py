class User:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


user1 = User("Alex")
user2 = User("ALEX")
print(user1 == user2)
