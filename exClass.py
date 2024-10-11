import keyboard
# Создать класс игрока, в котором будет 2 метода - идти вперед, идти назад, при продвижении вперед будет изменяться координата х игркока в +, назад в минус.

class Player():
    def __init__(self,name):
        self.name = name
        self.x = 0
        self.speed = 10

    def GoForward(self):
        self.x += self.speed

    def GoBack(self):
        self.x -= self.speed

player = Player("player1")

def on_press(key):
    if key.name == "up":
        player.GoForward()
    elif key.name == "down":
        player.GoBack()

    print(player.x)

def on_release(key):
    print(key)

keyboard.on_press(on_press)
keyboard.on_release(on_release)


keyboard.wait()