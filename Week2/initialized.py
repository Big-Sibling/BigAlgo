class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user2 = User()
user3 = User()
user4 = User()

user1.initialize("Young", "young@codeit.kr", "123456")
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
