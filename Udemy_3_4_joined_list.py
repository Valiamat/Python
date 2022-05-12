# на вход подаются 2 списка чисел длины N 
# нужно взять из 1 списка все четные а из второго все нечетные и объединить их в новом списке 

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
joined_list = []
for i in first_list:
    if i % 2 == 0:
        joined_list.append(i)
for i in second_list:
    if i % 2 == 0:
        joined_list.append(i)
print(f'Объединенный список: {joined_list}')
