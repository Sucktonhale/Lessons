def check_player_info_for_level(player_info:dict, lvl:int):
    res = False

    if player_info["lvl"] < lvl:
        res = player_info["money"] > 1000

    return res

def welcome_to_level(player_info):
    if check_player_info_for_level(player_info, 40):
        print("You're welcome, player!")
    else:
        print("You can not access level.")


player = {"lvl": 39, "money": 3399393939}
welcome_to_level(player)