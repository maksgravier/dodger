import tkinter
from time import sleep
from tkinter import mainloop, messagebox, simpledialog, Tk, Canvas
import time
root = Tk()
c = Canvas(root, height=300, width=300)
c.pack()
seconds = 0
minutes = 0
hours = 0

seconds_Text = c.create_text(30, 10, fill='blue', text='seconds:' + str(seconds))
minutes_Text = c.create_text(30, 20, fill='blue', text='minutes:' + str(minutes))
hours_Text = c.create_text(30, 30, fill='blue', text='hours:' + str(hours))

def count():
    global seconds, minutes, hours
    seconds += 1
    c.itemconfigure(seconds_Text, text='seconds:' + str(seconds))
    if seconds == 60:
        minutes += 1
        seconds = 0
        c.itemconfigure(seconds_Text, text='seconds:' + str(seconds))
        c.itemconfigure(minutes_Text, text='minutes:' + str(minutes))
    if minutes == 60:
        hours += 1
        minutes = 0
        c.itemconfigure(minutes_Text, text='minutes:' + str(minutes))
        c.itemconfigure(hours_Text, text='hours:' + str(hours))
    root.after(1000, count)

root.after(1000, count)
root.mainloop()


