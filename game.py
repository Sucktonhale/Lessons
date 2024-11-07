# Создать статический класс конфигурации, в нем будут следующие статические свойства - экран, движок, причем доступ к ним будет реализовываться только внутри самого класса,
# для простановки этих свойств будет использоваться метод Initialize - его нельзя вызывать дважды, если вызовешь второй раз он должен будет выкинуть Exception.
# Создать статический класс игры, у которого будут статические свойства - игрок и карта. Также у нее будет метод инициализации, который инициализирует конфиг, опять же дважды
# инициализировать нельзя - должна выдаваться ошибка. Также класс игры будет будет содержать статический метод старт, который просто выведет на экран любое сообщение.

class Config:
    __screen = None
    __engiene = None
    __inicializated = False

    @staticmethod
    def Initialize(__screen,__engiene):
        if not Config.__inicializated:
            Config.__screen = __screen
            Config.__engiene = __engiene
            Config.__inicializated = True
            print("Config Initialize sucsesfull")
        else:
            raise Exception("Something went wrong bla bla bla")

class Game:
    __player = None
    __map = None
    __inicializated = False

    @staticmethod
    def Initialize2(__player,__map):
        if not Game.__inicializated:
            Config.Initialize(None,None)
            Game.__map = __map
            Game.__player = __player
            Game.__inicializated = True
            print('Game Initialize sucsesful')
        else:
            raise Exception('Something went wrong again bla bla bla')

    @staticmethod
    def Start(__player,__map):
        if not Game.__inicializated:
            Game.Initialize2(__player, __map)
        else:
            Game.__player = __player
            Game.__map == __map

        print(f'Oh my god u r in our game congrats {Game.__player}')

Game.Initialize2("Avavaeff","fdf")
Game.Start('Avava','Dust2')
Game.Start('Avava3','Dust3')