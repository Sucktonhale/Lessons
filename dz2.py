def info_abut_user(ip,id,nick = ''):
   if nick:
       all_info = f'{ip} {id} {nick}'
   else:
       all_info = f"{ip} {id}"
   return all_info.title()
mellstroy = info_abut_user('23.45','188.45','helldrocher')
print(mellstroy)

def acc_reborn(password,nickname,age=52):
    user = {'pass':password,'name':nickname}
    if age:
        user['age'] = age
    return user
gamer = acc_reborn(12345,'John_Scina')
print(gamer)

def acc_reorn(password,nickname,age):
    user = f'{password} {nickname} {age} '
    return user.title()
while True:
    print(f'00010010101101101111010000001')
    P_par = input('00100101 : ')
    N_par = input('01000011001 :')
    A_par = int(input('00100100000102001 :'))

    User_data = acc_reorn(P_par,N_par,A_par)
    print(f'\nU ve been hacked,{User_data}:)')
