#Написать игру в "камень-ножницы-бумага" против компьютера.

#Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага). 
#Сгенерировать случайный выбор компьютера. Вывести выбор компьютера. Определить победителя, выведя соответствующую информацию. 
#Спросить пользователя - хочет ли он повторить игру. Если хочет - повторить, не хочет - выйти из цикла.
import random

play_again = True

while play_again == True:

    print('Введите R для камня, S для ножниц и P для бумаги')
    users_choice = input()
    
    if users_choice not in ["R", "S", "P"]:
        print("Введите корректное значение")
        continue
    
    computer_choice_options = ["R", "S", "P"]
    computer_choice = random.choice(computer_choice_options)
    #computer_choice = ("R")

    if users_choice == computer_choice:
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Ничья!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
    
    if users_choice == ("R") and computer_choice == ("S"):
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Вы выиграли!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
            
    if users_choice == ("R") and computer_choice == ("P"):
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Вы проиграли!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
            
    if users_choice == ("P") and computer_choice == ("S"):
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Вы проиграли!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
            
    if users_choice == ("P") and computer_choice == ("R"):
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Вы выиграли!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
            
    if users_choice == ("S") and computer_choice == ("R"):
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Вы проиграли!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
            
    if users_choice == ("S") and computer_choice == ("P"):
        print("Компьютер выбрал " + computer_choice + " , а вы выбрали " + users_choice)
        print("Вы выиграли!")
        continue_playing = input("Введите ДА, чтобы сыграть ещё раз. Введите НЕТ, чтобы закончить игру")
        if continue_playing == ("НЕТ"):
            break
