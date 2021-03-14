class Vector:
    def __init__(self,x=0,y=0):
        self.__x=0
        self.x=x
        self.__y=0
        self.y=y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if isinstance(x, int):
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        if isinstance(y,int):
            self.__y=y
                
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"{self.x:+}i{self.y:+}j"
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5
    def __neg__(self):
        return Vector(-self.x,-self.y)
    def __mul__(self, w):
        return self.x*w.x+self.y*w.y
    def __add__(self, w):
        return Vector(self.x+w.x,self.y+w.y)
if __name__=="__main__":
    v=Vector(3,4.1)
    u=Vector(x=2,y=4)
    print(v)
    print(abs(v))
    print (v.__add__(u))
