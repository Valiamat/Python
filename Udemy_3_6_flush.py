# в руке 2 карты, на столе 5 карт. Определить, есть ли флеш - 5 карт одной масти.
# карты записываем в формате J_S, где J - валет, а S - масть. Масти S=пики, H=червы, D=буби, C=трефы

table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]
both = table_cards + hand_cards
Hearts = "H"
Diamonds = "D"
Clubs = "C"
Spades = "S"
count_flush_C = 0
count_flush_S = 0
count_flush_H = 0
count_flush_D = 0

for x in range(len(both)):
    Is_True = both[x]
    if Is_True.endswith('S') == True:
        count_flush_S = count_flush_S+1

for x in range(len(both)):
    Is_True = both[x]
    if Is_True.endswith('C') == True:
        count_flush_C = count_flush_C+1

for x in range(len(both)):
    Is_True = both[x]
    if Is_True.endswith('H') == True:
        count_flush_H = count_flush_H+1

for x in range(len(both)):
    Is_True = both[x]
    if Is_True.endswith('D') == True:
        count_flush_D = count_flush_D+1
        
if count_flush_C >=5 or count_flush_S >=5 or count_flush_D >=5 or count_flush_H >=5:
    print ("Flush!")
else:
    print ("No Flush!")
