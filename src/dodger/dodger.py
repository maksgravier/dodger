from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font, mainloop

catcher_move_speed = 20
catcher_move_speed_2 = -20

canvas_width = 800
canvas_height = 400

#this makes the background and the title
root = Tk()
root.title('🚀 dodger')
c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue')
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.create_oval(400, 100, 300, 120, fill='white', width=0)
c.create_oval(400, 10, 1000, 120, fill='white', width=0)
c.create_rectangle(90, 300, 100, 200, fill='brown', width=0)
c.create_oval(50, 250, 140, 200, fill='green', width=0)
c.pack()


#informasion about the eggs
color_cycle = cycle(
    ['light blue', 'light green', 'light pink', 'light yellow', 'light cyan', 'violet', 'brown', 'black', 'white',
     'gray', 'dark orange', 'red'])
egg_width = 30
egg_height = 30
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

#informasion about the cacher
cacher_color = 'grey'
cacher_width = 50
cacher_height = 50
cacher_start_x = canvas_width / 2 - cacher_width / 2
cacher_start_y = canvas_height - cacher_height - 20
cacher_start_x2 = cacher_start_x + cacher_width
cacher_start_y2 = cacher_start_y + cacher_height

# draws the cacher
cacher = c.create_oval(cacher_start_x, cacher_start_y, cacher_start_x2, cacher_start_y2, fill=cacher_color, width=0)
game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)
score = 0

score_text = c.create_text(10, 10, anchor='nw', font=game_font, text='score: ' + str(score))

lives_remaning = 3
lives_Text = c.create_text(canvas_width - 10, 10, anchor='ne', font=game_font, fill='darkblue',
                           text='lives ' + str(lives_remaning))

#makeing a egg
eggs = []


def create_egg():
    x = randrange(10, 720)
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def tutorial(event):
    messagebox.showinfo('Welcome to dodger!!!!', 'the controls are wasd or arrow keys! see if you can dodge more than your friends and familiy good luck!')

#making it move


def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)


#game over or fell to the ground
def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    increase_score(egg_score)


#lose a life
def lose_a_life():
    global lives_remaning, score, egg_speed, catcher_move_speed, catcher_move_speed_2
    lives_remaning -= 1
    c.itemconfigure(lives_Text, text='lives: ' + str(lives_remaning))
    if lives_remaning == 0:
        messagebox.showinfo('game over!', 'final score:' + str(score))
        messagebox.showinfo('hint', 'if you lose it is okay')

        lives_remaning = 3
        score = 0
        egg_speed = 500
        catcher_move_speed_2 = - 20
        catcher_move_speed = 20
        c.itemconfigure(lives_Text, text='lives: ' + str(lives_remaning))
        c.itemconfigure(score_text, text='score: ' + str(score))


def restart(event):
    global lives_remaning, score, egg_speed, catcher_move_speed, catcher_move_speed_2
    lives_remaning = 3
    score = 0
    egg_speed = 500
    catcher_move_speed_2 = - 20
    catcher_move_speed = 20
    c.itemconfigure(lives_Text, text='lives: ' + str(lives_remaning))
    c.itemconfigure(score_text, text='score: ' + str(score))


#did you catch it
def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(cacher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if (egg_x2 > catcher_x and egg_x < catcher_x2) and \
                (egg_y2 > catcher_y and egg_y < catcher_y2):
            eggs.remove(egg)
            c.delete(egg)
            lose_a_life()
    root.after(100, check_catch)


#increase score

def increase_score(points):
    global score, egg_speed, egg_interval, catcher_move_speed, catcher_move_speed_2, restart
    score += points
    catcher_move_speed += 1
    catcher_move_speed_2 += -1
    if egg_speed > 50:
        egg_speed -= 10
    c.itemconfigure(score_text, text='score: ' + str(score))


#controls
def move_left(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if x1 > 0:
        c.move(cacher, catcher_move_speed_2, 0)


def move_right(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if x2 < canvas_width:
        c.move(cacher, catcher_move_speed, 0)


def move_up(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if y1 > 0:
        c.move(cacher, 0, catcher_move_speed_2)


def move_down(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if y2 < canvas_height:
        c.move(cacher, 0, catcher_move_speed)


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.bind('<Up>', move_up)
c.bind('<Down>', move_down)
c.bind('<a>', move_left)
c.bind('<d>', move_right)
c.bind('<w>', move_up)
c.bind('<s>', move_down)
c.bind('<space>', move_up)
c.bind('<Return>', restart)
c.bind('<?>', tutorial)
c.bind('</>', tutorial)
c.focus_set()
#starts the game
root.after(200, create_egg)
root.after(0, create_egg)
root.after(0, create_egg)
root.after(0, move_eggs)
root.after(1000, check_catch)
root.mainloop()