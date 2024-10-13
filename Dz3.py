class Cat():
    def __init__(self,name,age,damage):
        self.name = name
        self.age = age
        self.damage = damage
    def attack(self):
        print(f"{self.name} casted basic attac with dmg {self.damage}")
    def combo1(self):
        print(f"{self.name} made combo with dmg {self.damage} ")
my_cat = Cat('Chert',10,2500)
my_cat.attack()
my_cat = Cat("Chert",10,5070)
my_cat.combo1()
class Dog():
    def __init__(self,name):
        self.name = name
    def Sleep(self):
        print(f'{self.name} is sleeping :)')
my_dog = Dog('Willie')
my_dog.Sleep()