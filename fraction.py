#abstraction
#encapsulation
#وراثت
#چندريختي
class Fraction:
    def __init__(self,x=0,y=1):
        self.__x=0
        self.__y=1
        self.x=x
        self.y=y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        if isinstance(x,int):
            self.__x=x
            self.simplify()
        else:
            print("Error x!")
    @x.deleter
    def x(self):
        del self.__x
        
        
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        if isinstance(y,int) and y!=0:
            self.__y=y
            self.simplify()
        else:
            print("Error y!")
    @y.deleter
    def y(self):
        del self.__y
        
    def simplify(self):
        def mygcd(x,y):#x=30, #y=10 , x=10, y=0
            if y==0:
                return x
            return mygcd(y,x%y)
        bmm=mygcd(self.x,self.y)
        self.__x//=bmm
        self.__y//=bmm
    def __repr__(self):
        if self.y==1 or self.x==0:
            return f"{self.x}"
        return f"{self.x}/{self.y}"
    def __str__(self):
        if self.y==1 or self.x==0:
            return f"{self.x}"
        return f"{self.x}/{self.y}"
    def __abs__(self):
        return self.x/self.y
    def __mul__(self,g):
        return Fraction(self.x*g.x,self.y*g.y)
    def __add__(self,g):
        return Fraction(self.x*g.y+self.y*g.x,self.y*g.y)
    def __neg__(self):
        return Fraction(-self.x,self.y)
    def __sub__(self,g):
        return self+(-g)
    def __invert__(self):
        return Fraction(self.y,self.x)
    def __floordiv__(self,g):
        return Fraction(self.x*g.y,self.y*g.x)
    def __truediv__(self,g):
        return Fraction(self.x*g.y,self.y*g.x)
    def __lt__(self,g):
        return abs(self)<abs(g)
    def __le__(self,g):
        return abs(self)<=abs(g)
    def __eq__(self,g):
        return abs(self)==abs(g)
    def __neq__(self,g):
        return abs(self)!=abs(g)
        
f=Fraction(2,5)
p=Fraction(2,5)
g=Fraction(10,3)

print(f"f = {f}")
print(f"p = {p}")

print(f"g = {g}")
print(f"abs({f}) = {abs(f)}")
print(f"{f}*{g} = {f*g}")
print(f"{f}+{g} = {f+g}")
print(f"-{f} = {-f}")
print(f"{f}-{g} = {f-g}")
print(f"~{f} = {~f}")
print(f"{f}//{g} = {f//g}")
print(f"{f}/{g} = {f/g}")
print(f"{f}<{g} = {f<g}")
print(f"{f}<={g} = {f<=g}")
print(f"{f}=={g} = {f==g}")
print(f"{f}=={p} = {f==p}")
print(f"{f}!={g} = {f!=g}")
print(f"{f}!={p} = {f!=p}")
