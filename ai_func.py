'''Started on 22/01/2026 by Arqatron'''
import pymysql as py
class AI:
    def check_schema(self):
        self.cur.execute('SHOW DATABASES;')
        dbs=self.cur.fetchall()
        check=False
        for i in dbs:
            if i[0]=='AI_Data':
                check=True
                break
            else:
                check=False
        if check==False:    
            self.cur.execute('''CREATE DATABASE AI_Data''')
            self.cur.execute('''USE AI_Data;''')
            self.cur.execute('''CREATE TABLE Data( 
                             Words varchar(75) NOT NULL, 
                             Probability FLOAT(24) NOT NULL)''')
            return 'Created'
        else:
            pass
            return True
    def __init__(self):
        try:
            with open('Log.txt','r') as file:
                pass
        except FileNotFoundError:
            with open('Log.txt','w') as file:
                pass

        try:
           self.mycon=py.connect(user='root',host='localhost',password='sql123')
           self.cur=self.mycon.cursor()
           self.check_schema()
        except:
            with open('Log.txt','a') as file:
                file.write('\n')
                file.write('An error occured while initializing MySQL, please check your installation')
            
            print('An exception has occured: Please check the log for further details.')
            
    
    def calc(self,word,list_words):
        total=len(list_words)
        count=0
        for i in list_words:
            if i==word:
                count+=1
        prob=float(count/total)
        return prob
        
    def Train_input(self,sentence,truth=True):
        if truth:
            list_words=str(sentence).split(' ')
            self.cur.execute('USE AI_Data;')
            self.cur.execute('SELECT * FROM Data;')
            dat=self.cur.fetchall()
            for word in list_words:
                in_list=False
                for items in dat:
                    if items[0].lower()==word.lower() and (items[0].isspace()==False):
                        in_list=True
                        break
                    else:
                        in_list=False
                if in_list:
                    change=(1-(self.calc(word,list_words)))
                    self.cur.execute('''UPDATE Data SET Probability = %s WHERE Words = %s ''',(change,word))
                    self.mycon.commit()
                    continue
                elif in_list==False and word.replace(' ','')!='':
                    self.cur.execute(f"INSERT INTO Data VALUES(%s,1.0);",(word))
                    self.mycon.commit()
        else:
            pass
                        
    def extracted_data(self):
        self.cur.execute('USE AI_Data;')
        self.cur.execute('SELECT * FROM Data;')
        dat=self.cur.fetchall()
        data=[i for i in dat]
        return data
                

test=AI()
test.Train_input('     ')
