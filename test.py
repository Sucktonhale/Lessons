name = input("Enter your name: ")
passwrod = input("Enter password: ")

if passwrod == "1234":
    print(f"{name}, you're welcome!")


a = ["Name1", "Name2"]
print(a[0])

# Правая часть (а) - это откуда по очереди будем черпать элементы
# Левая часть (name) - это куда мы их будем класть по очереди
# Сам код отделенный табуляцией - это код, который выполнется для каждого вытащенного элемента
for name in a:
    print(name)

# len - length
# range - диапазон - диапазон чисел - range(3, 10) - от 3 до 9, range(10) - от 0 до 9
for i in range(len(a)):
    print(a[i])

x = 0

while x < 5:
    print(x)
    x += 1

# функция - это ЧЕРНЫЙ ЯЩИК, КОТОРЫЙ ВЫПОЛНЯЕТ КАКОЙ-ТО КОД, ИСПОЛЬЗУЯ ПРИСЛАННЫЕ НА ВХОД ДАННЫЕ И ЧТО-ТО ТЕБЕ ВОЗВРАЩАЕТ.
# (не обязательно возвращать, не обязательно принимать)
# y = x*5
def CheckPassword(password):
    return password == "12d"

pwd = input("Enter password: ")

if CheckPassword(pwd):
    print("You're welcome.")

user = {"name": "Name1", "pwd": "29ifd"}
print(user["name"])

for k in user.keys():
    print(k)

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_info(self):
        print(self.name)
        for item in self.inventory:
            print(item)

player = Player("Player1")
player.add_item("bow")
player.add_item("apple")
player.show_info()
