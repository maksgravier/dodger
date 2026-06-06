from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font, mainloop



#speed_up = 350
#move_one = 20from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font, mainloop


#speed_up = 350
#move_one = 20
#move_two = -20

canvas_width = 800
canvas_height = 400

#this makes the background
root = Tk()
root.title('🥚 egg cacher')
c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue' )
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.create_oval(400, 100, 300, 120, fill='white', width=0)
c.create_oval(400, 10, 1000, 120, fill='white', width=0)
c.create_rectangle(90, 300, 100, 200, fill='brown', width=0)
c.create_oval(50, 250, 140, 200, fill='green', width=0)
c.pack()

#informasion about the eggs
color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan', 'violet', 'brown', 'black', 'white', 'gray', 'dark orange'])
egg_width = 20
egg_height = 30
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

#informasion about the cacher
cacher_color = 'grey'
cacher_width = 100
cacher_height = 100
cacher_start_x = canvas_width / 2 - cacher_width / 2
cacher_start_y = canvas_height - cacher_height - 20
cacher_start_x2 = cacher_start_x + cacher_width
cacher_start_y2 = cacher_start_y + cacher_height

# draws the cacher
cacher = c.create_arc(cacher_start_x, cacher_start_y, cacher_start_x2, cacher_start_y2, start=200, extent=140, style='arc', outline=cacher_color, width=3)
game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)
score = 0

score_text = c.create_text(10, 10, anchor='nw', font=game_font, text='score: ' + str(score))

lives_remaning = 3
lives_Text = c.create_text(canvas_width - 10, 10,  anchor='ne', font=game_font, fill='darkblue', text='lives ' + str(lives_remaning))

#makeing a egg
eggs = []
def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

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
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('Game Over!', 'Final Score: ' + str(score))



#lose a life
def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_Text, text='lives: ' + str(lives_remaning))

#did you catch it
def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(cacher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 -egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)




#increase score

def increase_score(points):
    global score, egg_speed, egg_interval
    score +=points
    egg_speed = int(egg_speed * difficulty_factor)
    c.itemconfigure(score_text, text='score: ' + str(score))



#controls
def move_left(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if x1 > 0:
        c.move(cacher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if x2 < canvas_width:
        c.move(cacher, 20, 0)

def move_up(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if y1 > 0:
        c.move(cacher, 0, -20)


def move_down(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if y2 < canvas_height:
        c.move(cacher, 0, 20)


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.bind('<Up>', move_up)
c.bind('<Down>', move_down)
c.focus_set()

#starts the game
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()
#move_two = -20

canvas_width = 800
canvas_height = 400

#this makes the background
root = Tk()
root.title('🥚 egg cacher')
c = Canvas(root, width=canvas_width, height=canvas_height, background='deep sky blue' )
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.create_oval(400, 100, 300, 120, fill='white', width=0)
c.create_oval(400, 10, 1000, 120, fill='white', width=0)
c.create_rectangle(90, 300, 100, 200, fill='brown', width=0)
c.create_oval(50, 250, 140, 200, fill='green', width=0)
c.pack()

#informasion about the eggs
color_cycle = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan', 'violet', 'brown', 'black', 'white', 'gray', 'dark orange'])
egg_width = 20
egg_height = 30
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

#informasion about the cacher
cacher_color = 'grey'
cacher_width = 100
cacher_height = 100
cacher_start_x = canvas_width / 2 - cacher_width / 2
cacher_start_y = canvas_height - cacher_height - 20
cacher_start_x2 = cacher_start_x + cacher_width
cacher_start_y2 = cacher_start_y + cacher_height

# draws the cacher
cacher = c.create_arc(cacher_start_x, cacher_start_y, cacher_start_x2, cacher_start_y2, start=200, extent=140, style='arc', outline=cacher_color, width=3)
game_font = font.nametofont('TkFixedFont')
game_font.config(size=18)
score = 0

score_text = c.create_text(10, 10, anchor='nw', font=game_font, text='score: ' + str(score))

lives_remaning = 3
lives_Text = c.create_text(canvas_width - 10, 10,  anchor='ne', font=game_font, fill='darkblue', text='lives ' + str(lives_remaning))

#makeing a egg
eggs = []
def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

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
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('Game Over!', 'Final Score: ' + str(score))



#lose a life
def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_Text, text='lives: ' + str(lives_remaning))

#did you catch it
def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(cacher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 -egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)




#increase score

def increase_score(points):
    global score, egg_speed, egg_interval
    score +=points
    egg_speed = int(egg_speed * difficulty_factor)
    c.itemconfigure(score_text, text='score: ' + str(score))



#controls
def move_left(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if x1 > 0:
        c.move(cacher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if x2 < canvas_width:
        c.move(cacher, 20, 0)

def move_up(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if y1 > 0:
        c.move(cacher, 0, -20)


def move_down(event):
    (x1, y1, x2, y2) = c.coords(cacher)
    if y2 < canvas_height:
        c.move(cacher, 0, 20)


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.bind('<Up>', move_up)
c.bind('<Down>', move_down)
c.focus_set()

#starts the game
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()
