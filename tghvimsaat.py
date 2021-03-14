from taghvim import Taghvim
from zaman import Time
class TaghvimSaat(Taghvim,Time):
    def __init__(self,year=1,month=1,day=1,hour=10,minute=12,second=23):
        Taghvim.__init__(self,year,month,day)
        Time.__init__(self,hour,minute,second)
    def __str__(self):
        return Taghvim.__str__(self)+" "+Time.__str__(self)
    def __next__(self):
        Time.__next__(self)
        if Time.isMidnight(self):
            Taghvim.__next__(self)
        return self

if __name__=="__main__":
    ts=TaghvimSaat(1399,12,24,23,59,40)
    for i in range(30):
        print(next(ts))
