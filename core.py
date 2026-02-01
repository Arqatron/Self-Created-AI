'''Started on 22/01/2026 by Arqatron'''
import window_manager as winman
import ai_func
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.withdraw()
main=winman.window(root)
AI=ai_func.AI()


def Action_Train():
    
    def Confirm():
        dat=True
        if str(truth_opt.get())=="I'm telling the Truth":
            dat=True
        else:
            dat=False
        AI.Train_input(str(input_field.get()),dat)
        main.confirm_popup('Data has successfully been ingested.')
        
    Train_Frame=main.create_frame('Train_Frame')
    propmpt=tk.Label(Train_Frame,text='Enter Training Data:').pack()

    truth_opt=ttk.Combobox(Train_Frame,values=["I'm telling the Truth","I'm Lying"])
    truth_opt.pack()
    
    input_field=ttk.Entry(Train_Frame)
    input_field.pack()
    
    confirm_button=ttk.Button(Train_Frame,text='Confirm',command=lambda:Confirm())
    confirm_button.pack()
    
def Action_View_Data():
    View_Frame=main.create_frame('View Frame')
    table=ttk.Treeview(View_Frame,columns=('word','next','prob','count'),show='headings')

    table.heading('word',text='Word')
    table.heading('next',text='Next')
    table.heading('prob',text='Probability')
    table.heading('count',text='Total Count')

    for row in AI.extracted_data():
        table.insert('','end',values=row)
    table.pack(fill='both')
def Action_Chat():
    def generate_response(query=str(user_input.get())):
        response=AI.Response(query)
        
        
    Chat_Frame=main.create_frame('Chat Frame',400,500)
    user_input=ttk.Entry(Chat_Frame)
    user_input.place(x=190,y=390)
    send=ttk.Button(Chat_Frame,text='Send',command=generate_response)
    send.place(x=210,y=390)
    
main.create('Arq AI',600,800)
main.menubar_init()
main.menu_add('Action',[('Train',Action_Train),('View Data',Action_View_Data),('Chat',Action_Chat),('Log','')])


root.mainloop()
