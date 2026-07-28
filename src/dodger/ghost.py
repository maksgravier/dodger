# ghost game
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print('three doors ahead...')
    print('A ghost behind one')
    print('Wich door do you open')
    door = input('1, 2 or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('ghost!')
        feeling_brave = False
    else:
        print('No ghost!')
        print('you enter the next room.')
        score = score + 1
print('Run away!')
print('Game over! you scored ', score)
