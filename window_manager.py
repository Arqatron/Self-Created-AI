'''Started on 22/01/2026 by Arqatron'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql




class window:
    def __init__(self,root):
        self.root=root
        self.active_frame=None
    def create(self,name,height=400,width=500):
        self.menus={}
        
        self.name=tk.Toplevel(self.root)
        self.name.geometry(f'{width}x{height}')
        self.name.resizable(False,False)
        self.name.title(str(name))
       

    def menubar_init(self):
        self.menubar=Menu(self.name)
        self.name.config(menu=self.menubar)
        
        
    def menu_add(self, header,*options):
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

    def create_frame(self,frame_name,width=300,height=200,posx=20,posy=20):
        if self.active_frame!=None:
            self.active_frame.destroy()

        self.frame_name=tk.Frame(self.name,width=width,height=height)
        self.active_frame=self.frame_name
        self.frame_name.place(x=posx,y=posy)
        return self.frame_name
    
    def confirm_popup(self,message):
        self.conf_win=tk.Toplevel(self.name)
        self.conf_win.geometry('300x200')
        self.conf_win.resizable(False,False)

        msg=tk.Label(self.conf_win,text=str(message)).pack()
        okay=ttk.Button(self.conf_win,text='Confirm',command=self.conf_win.destroy).pack()





