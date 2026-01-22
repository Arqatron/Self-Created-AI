'''Started on 22/01/2026 by Arqatron'''
import pymysql as py
class AI:
    def __init__(self):
        try:
            with open('Log.txt','r') as file:
                pass
        except FileNotFoundError:
            with open('Log.txt','w') as file:
                pass

        try:
           mycon=py.connect(user='root',host='localhost',password='sql123')
        except:
            with open('Log.txt','a') as file:
                file.write('\n')
                file.write('An error occured while initializing MySQL, please check your installation')
            print('An exception has occured: Please check the log for further details.')
            
    
