#играем в кости. Кидаем 2 6гранника 3 раза, считаем сумму. 
#Если выпали дуплеты - сумма обнуляется, последующие броски не считаются. Вывести сумму.

lst = ([1,2], [3,4], [5,6])

def calc_dice_scores(lst):
    dice1 = lst[0]
    dice2 = lst[1]
    dice3 = lst[2]
    summ = dice1[0] + dice1[1] + dice2[0] + dice2[1] + dice3[0] + dice3[1]
    if dice1[0] == dice1[1] or dice2[0] == dice2[1] or dice3[0] == dice3[1]:
        summ = 0
    return summ
