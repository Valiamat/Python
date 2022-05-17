run_again = "Y"
while run_again == "Y":
    
    try:
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите второе число: "))
    except Exception as e:
        print("Error : {}".format(str(e)))
        print("Пожалуйста, введите числа снова")
        continue

    
    operation = input(''' 
    Выберите операцию 
    + для сложения
    - для вычитания 
    * для умножения
    / для деления 
    ''') 

    if operation == '+':
        print('{} + {} = '.format(num_1, num_2)) 
        print(num_1 + num_2) 
    elif operation == '-': 
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)
    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2) 
    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2))
        try:
            print(num_1 / num_2)
        except ZeroDivisionError:
            print('Ошибка! Деление на 0')
    else: print('Пожалуйста, введите корректный оператор')
    run_again = input("Нажмите Y, чтобы продолжить работу, или любую другую клавишу, чтобы завершить ")
