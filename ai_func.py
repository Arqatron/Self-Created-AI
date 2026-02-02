'''Started on 22/01/2026 by Arqatron'''
import pymysql as py
import math
import random
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
                             Next  varchar(75) NOT NULL,
                             Probability FLOAT(24) NOT NULL,
                             Count INT(10))''')
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
            
    def extracted_data(self):
        self.cur.execute('USE AI_Data;')
        self.cur.execute('SELECT * FROM Data;')
        dat=self.cur.fetchall()
        data=[i for i in dat]
        return data
    def calc(self,word,list_words):
        dat = self.extracted_data()
        recorded_count=1
        for items in dat:
            if items[0].lower()==word.lower():
                recorded_count=items[2]
                
        total=len(list_words)
        count=0
        for i in list_words:
            if i==word:
                count+=1
            
        prob=float(1-abs(count/total*recorded_count))
        return prob
        
    def Train_input(self,sentence,truth=True):
        if truth:
            list_words=str(sentence).split(' ')
            
            dat= self.extracted_data()
            for word in list_words:
                in_list=False
                
                for items in dat:
                    
                    
                    if items[0].lower()==word.lower() and (items[0].isspace()==False):
                        in_list=True
                        count=items[2]
                        break
                    else:
                        in_list=False
                next_word=''
                for i in range(len(list_words)):
                        try:
                            if list_words[i]==word:
                                next_word=list_words[i+1]
                        except:
                            next_word=''
                if in_list:
                        pair_exists=False
                        change=self.calc(word,list_words)
                        dat=self.extracted_data()
                        for items in dat:
                            if (items[0],items[1])==(word,next_word):
                                pair_exists=True
                                count=items[3]
                        if pair_exists:
                            self.cur.execute('''UPDATE Data SET Probability = %s WHERE Words = %s ''',(change,word))
                            
                            self.cur.execute('''UPDATE Data SET Count = %s WHERE Words = %s AND Next = %s''',(count+1,word,next_word))
                            self.mycon.commit()

                            try:
                                with open('Log.txt','a') as file:
                                    file.write('\n')
                                    file.write(f'Probability and count for ({word},{next_word}) were changed')
                            except FileNotFoundError:
                                with open('Log.txt','w') as file:
                                    file.write('\n')
                                    file.write(f'Probability and count for ({word},{next_word}) were changed')
                        else:
                            self.cur.execute("INSERT INTO Data VALUES(%s,%s,%s,%s);",(word,next_word,1.0,1))
                            self.mycon.commit()
                            try:
                                with open('Log.txt','a') as file:
                                    file.write('\n')
                                    file.write(f'New word pair ({word},{next_word}) was added')
                            except:
                                with open('Log.txt','a') as file:
                                    file.write('\n')
                                    file.write(f'New word pair ({word},{next_word}) was added')
                                
                            continue
                elif in_list==False and word.replace(' ','')!='':
                            self.cur.execute("INSERT INTO Data VALUES(%s,%s,%s,%s);",(word,next_word,1.0,1))
                            self.mycon.commit()
                            try:
                                with open('Log.txt','a') as file:
                                    file.write('\n')
                                    file.write(f'New word pair ({word},{next_word}) was added')
                            except:
                                with open('Log.txt','a') as file:
                                    file.write('\n')
                                    file.write(f"New word pair {word},{next_word} was added")
        else:
            pass
                        
    
    def Response(self,sentence):
        self.Train_input(sentence)
                   
        self.response=''
                   
        self.type='statement'

        self.tense='Present'
                   
        Q_tags=('what','when','where','why','how','?')
                   
        Tenses={'Present':'is','Past':'was','Future':'will'}
        
        words=str(sentence).rstrip().lstrip().split(' ')
                 
        for i in words:
            if (i.lower() in Q_tags) and (words[-1][-1]=='?'):
                self.type='question'
                break
            else:
                self.type='statement'
                
        for word in words:
            if word==Tenses['Present']:
                self.tense='Present'
            elif word==Tenses['Past']:
                self.tense='Past'
            elif word==Tenses['Future']:
                self.tense='Future'
                    
        data=sorted(self.extracted_data(), key= lambda x:x[1])
        
        for i in range(len(data)):
            temp=random.randint(0,i)
            data[i],data[temp]=data[temp],data[i]
        
        
        for i in range(len(data)):
            try:
                if (data[i][2]>0.6 or data[i][1]==data[i+1][0]) and len(self.response)<250:
                        self.response+=data[i][0]
                        self.response+=' '
                        self.response+=data[i][1]
                        self.response+= ' '
                        if len(self.response)%10==0:
                            self.response+='\n'
            except:
                break
        self.Train_input(self.response)
        return self.response
          


