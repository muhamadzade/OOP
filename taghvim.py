"""
Javad Mohammadzadeh
Date:24/12/99
Taghvim
31,31,31,31,31,31,30,30,30,30,30,29
"""
class Taghvim:
    monthsName=("","فروردين","ارديبهشت","خرداد",
                "تير","مرداد","شهريور",
                "مهر","آبان","آذر",
                "دي","بهمن","اسفند")
    months=(0,31,31,31,31,31,31,30,30,30,30,30,29)
    def __init__(self,year=1,month=1,day=1):
        self.__year=1
        self.__month=1
        self.__day=1
        self.year=year
        self.month=month
        self.day=day
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,year):
        if isinstance(year,int) and year>0:
            self.__year=year
        else:
            print("Year Error")
            
    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self,month):
        if isinstance(month,int) and 0<month<13:
            self.__month=month
        else:
            print("Month Error")

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self,day):
        if isinstance(day,int) and 0<day<=self.months[self.month]:
            self.__day=day
        else:
            print("Day Error")

    def __str__(self):
        return f"{self.year:04}/{self.month:02}/{self.day:02}"
    def __repr__(self):
        return f"{self.year%100:02}/{self.monthsName[self.month]}/{self.day:02}"

    def __next__(self):
        self.__day+=1
        if self.months[self.month]<self.__day:
            self.__day=1
            self.__month+=1
            if self.__month==13:
                self.__month=1
                self.__year+=1
        
        return self
    
if __name__=="__main__":
    t=Taghvim(1399,12,24)
    for i in range(365):
        print(next(t))
        



        
