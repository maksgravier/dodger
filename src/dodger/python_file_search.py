import runpy
from runpy import *
import tkinter
from tkinter import messagebox, simpledialog, Tk

def main():

        try:
            search = simpledialog.askstring('search for one of my games', prompt='search for one of my games')
            search_prossessed = search + '.py'
            runpy.run_path(search_prossessed)
            main()
        except FileNotFoundError:
            messagebox.showerror('error', message='something went wrong')
            main()



main()
