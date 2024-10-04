def info_abut_user(ip,id,nick = ''):
   if nick:
       all_info = f'{ip} {id} {nick}'
   else:
       all_info = f"{ip} {id}"
   return all_info.title()
mellstroy = info_abut_user('23.45','188.45','helldrocher')
print(mellstroy)

def acc_reborn(password,nickname):
    user = {'pass':password,'name':nickname}
    if age:
        user['created'] = age
    return user
gamer = acc_reborn(12345,'John_Scina',age = 52)
print(gamer)