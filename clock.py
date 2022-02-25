class Clock:
    def __init__(self,hour=10,
                 minute=12,second=23,op=1):
        self.__hour=0
        self.__minute=0
        self.__second=0
        self.hour=hour
        self.minute=minute
        self.second=second
        if op==2:
            import datetime
            now=datetime.datetime.now()
            self.hour=now.hour
            self.minute=now.minute
            self.second=now.second
        if op==3:
            self.input_()
            
    def input_(self):
        self.hour=int(input("hour = "))
        self.minute= int(input("minute = ")) 
        self.second=int(input("second = "))
        
    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self,hour):
        if isinstance(hour,int) and 0<=hour<24:
            self.__hour=hour
        else:
            print("error hour!")
            

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self,minute):
        if minute in range(60):
            self.__minute=minute
        else:
            print("error minute!")
            
    
    def getSecond(self):
        return self.__second
    def setSecond(self,second):
        if second in range(60):
            self.__second=second
        else:
            print("error second!")
    second=property(getSecond,setSecond)

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
    def __repr__(self):
        if self.hour<12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} AM"
        elif self.hour==12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} PM"
        else:
            return f"{self.hour-12:02}:{self.minute:02}:{self.second:02} PM"
            
    def tik(self):
         self.__second=(self.__second+1)%60
         if not self.__second:
             self.__minute=(self.__minute+1)%60
             if not self.__minute:
                 self.__hour=(self.__hour+1)%24

    def __next__(self):
        self.tik()
        return self

    def run(self):
        import os
        import time
        while True:
            print(next(self))
            time.sleep(1)
            self.ding()
            os.system("cls")
            
    def isMidnight(self):
        return not (self.hour or self.minute or self.second)
    def isOnHour(self):
        return not (self.minute or self.second)
        
    def ding(self):
        from winsound import Beep
        if self.isMidnight():
            print(24*"ding ")
            Beep(600,1000)
        elif self.isOnHour():
            print(self.hour*"ding ")
            for i in range(self.hour):
                Beep(2000,1000)
    def ding2(self):
        from playsound import playsound
        if self.isMidnight():
            playsound('ding.mp3')
        elif self.isOnHour():
            for i in range(self.hour):
                playsound('ding.mp3')


if __name__=="__main__":
    t=Clock(hour=23,minute=59,second=58)
    t.run()
