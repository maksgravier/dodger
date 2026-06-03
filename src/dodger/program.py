import tkinter
from tkinter import *
import random
from random import *


width = 2000
height = 1000
move_inform = 10


root = Tk()
root.title('space invader')
c = Canvas(root, width=width, height=height, background='black' )
c.pack()

player_actual = c.create_oval(50, 50, 250, 250, fill='light blue')

global enemys
enemys = []

def create_enemy():
    PLACE = randrange(0, width-50, 50)
    enemy = c.create_oval(PLACE, 0, PLACE+50, 50, fill='red')
    enemys.append(enemy)
    return enemy

def move_enemy():
    for enemy in enemys:
        c.move(enemy, 0, 20)
    root.after(200, move_enemy)


def left(event):
    c.move(player_actual, -move_inform, 0 )
    


def right(event):
    c.move(player_actual, move_inform, 0 )

def up(event):
    c.move(player_actual, 0, -move_inform)

def down(event):
    c.move(player_actual, 0, move_inform)

root.bind('a', left)
root.bind('d', right)
root.bind('w', up)
root.bind('s', down)
root.bind('A', left)
root.bind('D', right)
root.bind('W', up)
root.bind('S', down)

root.after(1000, create_enemy)
root.after(0, move_enemy)
root.mainloop()