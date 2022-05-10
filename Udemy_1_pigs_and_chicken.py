# На ферме есть куры, коровы и свиньи. У курицы две ноги, у свиньи - четыре, у коровы - четыре. 
# Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров, 
# просуммировать кол-во ног всех животных и вывести результат на консоль.
cows_str = input('Сколько у вас коров?')
pigs_str = input('Сколько у вас свиней?')
chicken_str = input('Сколько у вас куриц?')
cows = int(cows_str)
pigs = int(pigs_str)
chicken = int(chicken_str)
cows_legs = cows*4
pigs_legs = pigs*4
chicken_legs = chicken*2
print (cows_legs + pigs_legs + chicken_legs)
 
