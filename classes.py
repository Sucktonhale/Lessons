user = {"username": "2123", "pwd": "123132"}
username = user["username"]

try:
    pwd = user["pwed"]
except KeyError:
    print("pwed key not found")
except Exception:
    print("exception was thrown")


def clear_user_password(user : dict):
    password = user.pop("pwd")  # pop - вытащить с удалением
    return password

p = clear_user_password(user)
print(p)
print(user)

class User:
    def __init__(self, userName, userPassword):
        self.name = userName
        self.password = userPassword

    def clear_password(self):
        pwd = self.password
        self.password = None
        return pwd

user2 = User("8user", "diofh8wfdfsdf")  # init
print(user2.name)
print(user2.password)

print(user2.clear_password())
print(user2.password)
user3 = User("name", "pwd")
print(user3.password)
print(user2)