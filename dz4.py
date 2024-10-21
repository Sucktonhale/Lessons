class User:
    def __init__(self,usrname,pwd):
        self.name = usrname
        self.pwd = pwd
    def ban_user(self):
        print(f'u,ve been banned beacuase ur name {self.name} contains letters')
user1 = User('Gfe',3256)
user2 = User('hted',76487)
user1.ban_user()

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def laydown(self):
        print(f'{self.name} is lay now')
    def info_about_animal(self):
        print(f'ur pet is {self.age} old and his name is {self.name}')
class Puppy:
    def __init__(self,name,age,colour):
        super().__init__(name,age)
        self.name = name
        self.colour = colour
    def makeEyes(self):
        print(f'ur {self.name} is make eyes and have eyes colour {self.colour}')
my_puppy = Puppy('Tom',5,'black')
my_puppy.makeEyes()