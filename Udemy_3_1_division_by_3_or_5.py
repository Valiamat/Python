# получаем на ввод число и в цикле от 0 до введенного числа считаем сумму всех чисел делящихся на 3 или 5 без остатка


limit = int(input ("Введите число: "))
total_sum = sum([i for i in range (limit + 1) if i%3 == 0 or i%5 == 0])
print(total_sum)
 
