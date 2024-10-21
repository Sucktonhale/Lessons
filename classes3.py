
class Item2:
    def __init__(self, name, coast):
        self.name = name
        self.coast = coast

class Player:
    def __init__(self, username, health, damage):
        self.usernmae = username
        self.health = health
        self.damage = damage
        self.__inventory = []   # __ - скрывают видимость за пределами класса

    def __can_add(self):
        return len(self.__inventory) < 20

    def add_item(self, item : Item2):
        if item.__class__.__name__ != Item2.__name__:
            raise Exception(f"{item} is not Item.")

        if self.__can_add():
            self.__inventory.append(item)

            return True

        return False

    def show_inventory(self):
        for item in self.__inventory:
            print(f"{item.name} .. {item.coast} RUB")


player = Player("22", 23,32)
player.add_item(Item2("apple", 23))
player.add_item(23)
player.show_inventory()
