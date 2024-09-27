sportsmens = ['david','sam','tom']
for sportsman in sportsmens:
     print('you re realy strong',sportsman)
#Пример 1
sportsmens = ['david','sam','tom']
for sportsman in sportsmens:
     print(f'{sportsman.title()},that was cool!.\n')
#Пример 2
sportsmens = ['david','sam','tom']
for sportsman in sportsmens:
     print(f'ill bye a ticket to your next show {sportsman.title()}.\n')

x = 3
a = f"hello world {x}"
#Пример 3
sportsmens = ['david','sam','tom']
for sportsman in sportsmens:
     print(f'ill bye a ticket to your next show {sportsman.title()}.\n')
print("Bye dear spectators")
players = ['player01','player02','player03','player04','player05']
print(players[1:3])
#Пример 4
print('here is 4 players on tournament ')
for player in players[:4]:
 print(player.title())
 #Пример 5
 my_games = ['Rust','minecraft','roblox','terraria','cuphead']
 friend_games = my_games[:]
 print('games on my pc')
 print(my_games)
 print('\ngames on friend pc')
 print(friend_games)
 #Пример 6
 my_games = ['Rust','minecraft','roblox','terraria','cuphead']
 friend_games = my_games
 my_games.append('counter strike 2')
 print('games on my pc')
 print(my_games)
 print('\ngames on friend pc')
 print(friend_games)
 #Словари ееее эщкере

 nicknames = {'user01':'Gojo_Satoru','user02':'САХАРОК','user03':'Yafa_Shist'}
 print(nicknames['user02'])
 new_nicks = nicknames['user03']
 print(f'You was registered successfull {new_nicks},congrats')
 #пример 7
 streamers = {}
 streamers['streamer01'] = ['Stint']
 streamers['streamer02'] = ['Toxat2x2']
 print(streamers)
#funchii
 def ban_user():
      print("U was banned for exploting")
 ban_user()

def unban_user(username):
     print(f"U was unbannded,{username.title()}!")
unban_user('Suckthale')

def describe_pet(animal_type, pet_name):
    "information about animal"
    print(f"\nI have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','musorka')
describe_pet('cat','dik')

def describe_pet( pet_name,animal_type = 'homyak'):
    "information about animal"
    print(f"\nI have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='eblusha')

