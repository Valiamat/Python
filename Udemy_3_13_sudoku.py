#функция которая принимает двухмерный массив 3*3 и возвращает false если все числа от 1 до 9 встречаются ровно 1 раз,
# если встречаются не один раз - вернуть true

def any_duplicates(square):
    dice1 = square[0]
    dice2 = square[1]
    dice3 = square[2]
    summ = dice1[0] + dice1[1] + dice1[2] + dice2[0] + dice2[1] + dice2[2] + dice3[0] + dice3[1] + dice3[2]
    print(summ)
    if summ == 45:
        return False
    else:
        return True
