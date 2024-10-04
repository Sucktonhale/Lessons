# Написать фунцию,которая примет в себя количество денег игрока, его уровень и вернет истину, если у него дене больше 100 И уровень меньше 10, иначе вернет лоожь
def account(money,lvl):
    if money >= 100 and lvl <= 10:
        return True
    else:
        return False

res_false = account(65,15)    # false
res_true = account(400, 8)  # true

print(f"res_true: {res_true}")
print(f"res_false: {res_false}")



print(f"res1: {account(5,699)}")

def account_simplify(money,lvl):
    return money >= 100 and lvl <= 10

res_false = account_simplify(65,15)    # false
res_true = account_simplify(400, 8)  # true

print(f"res_true 2: {res_true}")
print(f"res_false 2: {res_false}")