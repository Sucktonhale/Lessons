class Cat():
    def __init__(self,name,age,damage):
        self.name = name
        self.age = age
        self.damage = damage
    def attack(self):
        print(f"{self.name} casted basic attac with dmg {self.damage}")
    def combo1(self):
        print(f"{self.name} made combo with dmg {self.damage} ")
