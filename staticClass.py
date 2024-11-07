from dz4 import user2


class Game:
    __config = None
    __map = None
    __initialized = False

    @staticmethod
    def Initialize(config, map):
        if not Game.__initialized:
            Game.__config = config
            Game.__map = map
            Game.__initialized = True
            print("Initialized!")

class User:
    key = "USER"

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show_info(self):
        print(self.name, self.password)

    @staticmethod
    def Deserialize(dictUser: dict):
        username = dictUser.get("name")
        pwd = dictUser.get("password")

        if username == None or pwd == None:
            raise Exception("Empty data.")

        return User(username, pwd)


Game.Initialize("conf", "map")
Game.Initialize("conf", "map")
Game.Initialize("conf", "map")
Game.Initialize("conf", "map")



userDict = {"name": "test", "password": "as9a0suda"}
user = User.Deserialize(userDict)
print(user.name)

testDict = {"aha": "123"}
user2 = User.Deserialize(testDict)