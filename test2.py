# UIElement базовый класс, в нем есть свойство -  ширина, высота и метод отрисовки. Класс Text наследуется от UIElement и
# имеет дополнительные свойства, которых не
# хвататет для ТЕКСТА (цвет может быть и т.д.), также есть Button - которая такой же UIElement, но у него есть ТЕКСТ.
class UIELement:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def Draw(self):
        print(f'Отрисован {self.__class__.__name__}')

class Text(UIELement):
    def __init__(self,width,height,Colour,font):
        super().__init__(width,height)
        self.Colour = Colour
        self.font = font

class Button(UIELement):
    def __init__(self,width,height,Colour,text):
        super().__init__(width,height)
        self.Colour = Colour
        self.txt = text

buton = Button(25,25,'Purple','Play')
uielement = UIELement(50,500)
uielement.Draw()
text = Text(10,10,"Green",'Calibry')
buton.Draw()
text.Draw()