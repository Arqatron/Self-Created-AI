'''Started on 22/01/2026 by Arqatron'''
import window_manager as winman
import tkinter as tk

root=tk.Tk()
root.withdraw()



main=winman.window(root)
main.create('Arq AI')
main.menubar_init()
main.menu_add('Action',[('Train',''),('View Data',''),('Search',''),('Log','')])


root.mainloop()
