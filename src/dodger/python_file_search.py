import runpy
from runpy import *
import tkinter
from tkinter import messagebox, simpledialog, Tk

def main():

        try:
            search = simpledialog.askstring('search for a file', prompt='search for a file')
            search_prossessed = search + '.py'
            runpy.run_path(search_prossessed)
            main()
        except FileNotFoundError:
            messagebox.showerror('error', message='something went wrong')
            main()



main()
