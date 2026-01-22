'''Started on 22/01/2026 by Arqatron'''
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import pymysql




class window:
    def __init__(self,root):
        self.root=root
    def create(self,name,height=400,width=500):
        self.menus={}
        
        self.name=tk.Toplevel(self.root)
        self.name.geometry(f'{width}x{height}')
        self.name.resizable(False,False)
        self.name.title(str(name))
       

    def menubar_init(self):
        self.menubar=Menu(self.name)
        self.name.config(menu=self.menubar)
        
        
    def menu_add(self, header, *options):
        self.menus[header] = options
        
        self.menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=header, menu=self.menu)
        for i in options:
            
            for j in i:
               self.menu.add_command(label=j[0],command=j[1])

        
    def del_option(self, name):
          for header in self.menus.keys():
              for opts in self.menus[header]:
                        temp=[]
                        for rec in opts:
                            if rec[0].lower()!=name.lower():
                               temp.append(rec)
                        self.menubar.delete(header)
                        self.menus[header]=temp
                        self.menu_add(header,tuple(temp))
                       
    def del_header(self,name):
        if name in self.menus.keys():
            self.menubar.delete(name)
        
    






