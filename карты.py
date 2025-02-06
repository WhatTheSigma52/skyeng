from random import shuffle
from random import randint

a = []
diler = []
player = []
cards = []
i = 0
count_player = 0
count_diler = 0

user = int(input('enter 1 to start: '))

if user == 1:
    end = randint(1, 2)

    for card in range(2, 11):
        for shape in range(4):
            cards.append(card)
    cards += ['ace', 'queen', 'king', 'jack'] * 4
    shuffle(cards)

    for i in cards:
        if len(diler) > 1:
            break
        diler.append(cards.pop(cards.index(i)))
    for h in cards:
        if len(player) > 1:
            break
        player.append(cards.pop(cards.index(h)))
      
           
    print('')
    print(f"yours cards: {player[0]}, {player[1]}")

    question = input('enter "pass" to stop the game and enter "take" to take one card: ')

    while question != "pass":
        for g in cards:
            player.append(cards.pop(cards.index(g)))
            break
        for u in cards:
            diler.append(cards.pop(cards.index(u)))
            break
        print(f'your cards: {player}')

        question = input('enter "pass" to stop the game and enter "take" to take one card: ')
    else:
        for count in player:
            if count == 'king':
                count_player += 10
            elif count == 'queen':
                count_player += 10
            elif count == 'jack':
                count_player += 10
            elif count == 'ace':
                ace_player = int(input('choose ace: 11 or 1 (enter the number): '))   
                if ace_player == 1:
                    count_player += 1
                else:
                    count_player += 11
            else:
                count_player += count
        for countdiler in diler:
            if count_diler > 17:
                break
            if countdiler == 'king':
                count_diler += 10
            elif countdiler == 'queen':
                count_diler += 10
            elif countdiler == 'jack':
                count_diler += 10
            elif countdiler == 'ace':
                if count_diler < 11:
                    count_diler += 11
                else:
                    count_diler += 1
            else:
                count_diler += countdiler
    print(f'yours points: {count_player}')
    print(f"diler's points: {count_diler}")
    
    if count_diler > count_player and count_diler > 16 and count_diler < 22:
        print('diler won')
    elif count_diler < count_player and count_diler > 16 and count_diler < 22:
        print('player won')
    elif count_diler > count_player and count_player > 22:
        print('player won')
    elif count_player > 21 or count_player < 17:
        print('diler won')
    elif count_diler < 17 and count_player > 21:
        print('no one won')
    elif count_player < 17 and count_diler > 21:
        print('no one won')
    elif count_player == 21 and count_diler == 21:
        print('you got 21 both. then 1 - win player, 2 - win diler: ')
        print(end)
        if end == 1:
            print('player won')
        else:
            print('diler won')
    elif count_diler > count_player and count_player < 17 and count_diler < 17:
        print('diler won')
    elif count_diler < count_player and count_player < 17 and count_diler < 17:
        print('player won')
    elif count_diler < count_player and count_diler > 16 and count_diler < 22 and count_player > 21:
        print('diler won')
    else:
        print('player won')
        
