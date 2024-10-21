from random import randint


class Entity:
    def __init__(self, name, health, damage):
        self.name = name
        self.health  = health
        self.damage = damage
        self.inventory = []

    def Atack(self, entity):
        entity.health -= 1

class Mob(Entity):
    def __init__(self, name, health, damage, capacity):
        super().__init__(name, health, damage)
        self.capacity = capacity
        self.x = 0
        self.y = 0

    def AutoRun(self):
        self.x += randint(10)
        self.y += randint(10)

enity = Entity("ff", 123,123)
mob = Mob("fd", 34,23, "dfdf")
mob.Atack(enity)