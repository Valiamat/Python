# Запросить у пользователя координаты x и y двух точек на плоскости. Посчитать расстояние между заданными точками 
# и вывести результат на консоль с точностью до трёх знаков после запятой (плавающей точки).
import math 
Xx_str = input('Введите ось X точки x')
Xx = int(Xx_str)
Yx_str = input('Введите ось Y точки x')
Yx = int(Yx_str)
Xy_str = input('Введите ось X точки y')
Xy = int(Xy_str)
Yy_str = input('Введите ось Y точки y')
Yy = int(Yy_str)
rasst = math.sqrt((Xx-Xy)**2+(Yx-Yy)**2)
rasst_okr = round(rasst, 3)
print(rasst_okr)
 
 
