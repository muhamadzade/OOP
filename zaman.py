class Time:
    def __init__(self,hour=10,minute=12,second=23):
        self.__hour=10
        self.__minute=12
        self.__second=23
        self.hour=hour
        self.minute=minute
        self.second=second
    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self,hour):
        if isinstance(hour,int) and 0<=hour<24:
            self.__hour=hour
        else:
            print("Ivalid hour")
            
    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self,minute):
        if isinstance(minute,int) and 0<=minute<60:
            self.__minute=minute
        else:
            print("Ivalid minute")


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self,second):
        if isinstance(second,int) and 0<=second<60:
            self.__second=second
        else:
            print("Ivalid second")

    def isMidnight(self):
        return self.hour==0 and self.minute==0 and self.second==0
    def ding(self):
        import winsound
        def music():
            for i in range(5):
                winsound.Beep(300,100)
                winsound.Beep(300,100)
                winsound.Beep(300,100)
                winsound.Beep(800,100)
        def musicR():
            import random
            for i in range(5):
                winsound.Beep(random.randrange(50,3000),100)
                winsound.Beep(random.randrange(50,3000),200)
                winsound.Beep(random.randrange(50,3000),300)
                winsound.Beep(random.randrange(50,3000),500)
        if self.isMidnight():
            musicR()    
##            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            print("Ding Ding Ding")

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
        if self.__second==0:
            self.__minute=(self.__minute+1)%60
            if self.__minute==0:
                self.hour=(self.hour+1)%24
    def __next__(self):
        self.tik()
        self.ding()
        return self
if __name__=="__main__":
    t=Time(23,59,20)
    for i in range(60):
        print(next(t))
else:
    print("Welcome to Time class")
