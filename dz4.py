class User():
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
    def ban_user(self):
        print(f'u,ve been banned beacuase ur name {self.name} contains letters')
user1 = User('Gfe',3256)
user2 = User('hted',76487)
user1.ban_user()