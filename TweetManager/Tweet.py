import time
import datetime

class Tweet():
    
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = datetime.datetime.now()

    def getAuthor(self):
        return self.__author

    def getText(self):
        return self.__text
    
    def getAge(self):
        time = datetime.datetime.now()
        time = time - self.__age
        time = time.seconds
        if(time<60):
            return str(time)+"s"
        elif(time > 60 and time <36000):
            
            return str(time/60)+"m"
        else:
            return str(time/360)+"h"
