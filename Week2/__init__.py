class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User("jihwan","jihwan@email.com","hihi")
user2 = User("jihwa","jihwa@email.com","hih")
user3 = User("jihw","jihw@email.com","hi")
user4 = User("jih","jih@email.com","h")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)