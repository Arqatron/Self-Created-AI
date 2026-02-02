'''Started on 22/01/2026 by Arqatron'''
import window_manager as winman
import ai_func
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root=tk.Tk()
root.withdraw()
main=winman.window(root)
AI=ai_func.AI()


def Action_Train():
    
    def Confirm(code):
        if code=='MI':
            dat=True
            if str(truth_opt.get())=="I'm telling the Truth":
                dat=True
            else:
                dat=False
            if dat:
                AI.Train_input(str(input_field.get()),dat)
                main.confirm_popup('Data has successfully been ingested.')
            
        elif code=='FI':
            def finish_training(data):
                if str(truth_opt.get())=="I'm telling the Truth":
                    dat=True
                else:
                    dat=False
                if dat:
                    for lines in data:
                        AI.Train_input(lines)
                    main.confirm_popup('Data has successfully been ingested')
            path=filedialog.askopenfilename(filetypes=[('All files','*.txt')])
            try:
                with open(path,'r') as file:
                    data=file.readlines()
                final_conf=ttk.Button(interface_container,text='Confirm File Upload',command=lambda:finish_training(data))
                final_conf.place(x=250,y=200)
            except:
                pass
                
    Train_Frame=main.create_frame('Train_Frame',800,500)
    
    interface_container=tk.LabelFrame(Train_Frame,width=600,height=500,text='Train')
    interface_container.place(x=20,y=20)
    
    
    
    truth_opt=ttk.Combobox(interface_container,values=["I'm telling the Truth","I'm Lying"])
    truth_opt.place(x=250,y=300)
    
    input_field=ttk.Entry(interface_container)
    input_field.place(x=250,y=345)
    
    confirm_button=ttk.Button(interface_container,text='Confirm',command=lambda:Confirm('MI'))
    confirm_button.place(x=250,y=415)

    file_upload=ttk.Button(interface_container,text='Upload text file...',command=lambda:Confirm('FI'))
    file_upload.place(x=250,y=100)
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
    Chat_Frame=main.create_frame('Chat Frame',800,500)
    def generate_response():
        query=str(user_input.get())
        if len(query.strip())>0:
            user_input.delete(0,'end')
            response=AI.Response(query)
            out.config(text=response)
        else:
            pass
        
    
    
    
    out_container=tk.LabelFrame(Chat_Frame,text='Chat',width=600,height=500)
    out_container.place(x=150,y=0)

    user_input=ttk.Entry(out_container)
    user_input.place(x=190,y=390)
    
    send=ttk.Button(out_container,text='Send',command=lambda:generate_response())
    send.place(x=400,y=390)

    
    out=tk.Label(out_container,text='')
    out.place(x=20,y=20)
def Action_Log():
    Log_Frame=main.create_frame('Log Frame',800,500)
    Log_out=tk.LabelFrame(Log_Frame,width=500,height=500,text='Log')
    Log_out.pack()
    scrollbar=tk.Scrollbar(Log_Frame)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    with open('Log.txt','r') as file:
        file.seek(0)
        data=file.read()
    
    out=tk.Text(Log_out,width=100,height=200,yscrollcommand=scrollbar.set)
    out.pack()
    for i in data:
        out.insert(tk.END,str(i))

    
    
main.create('Arq AI',600,800)
main.menubar_init()
main.menu_add('Action',[('Train',Action_Train),('View Data',Action_View_Data),('Chat',Action_Chat),('Log',Action_Log)])


root.mainloop()
