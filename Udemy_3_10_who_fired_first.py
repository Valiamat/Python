#whos_first = (
#"    Bang!  ",
#"   Bang!"
#)
#p1 стреляет быстрее p2

#мое решение

def whos_first(p1, p2):
    bangtuple = (p1, p2)
    player1 = list(bangtuple[0]) 
    player2 = list(bangtuple[1])
    for i in range(len(player1)):
        if player1[i] == 'B' and player2[i] != 'B': 
            return 'p1'
        elif player2[i] == 'B' and player1[i] != 'B': 
            return 'p2'
        elif player1[i] == 'B' and player2[i] == 'B': 
            return 'Tie!'
