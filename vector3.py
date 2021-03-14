from vector import Vector
class Vector3D(Vector):
    def __init__(self, x=0,y=0,z=0):
        Vector.__init__(self,x,y)
        self.__z=0
        self.z=z

    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, z):
        if isinstance(z, int):
            self.__z = z

    def __str__(self):
        return Vector.__str__(self)[:-1] + f",{self.z})"
    def __repr__(self):
        return Vector.__repr__(self)+f"{self.z:+}k"
    def __abs__(self):
        return (Vector.__abs__(self)**2+self.z**2)**0.5
    def __neg__(self):
        return Vector3D(-self.x,-self.y,-self.z)
    def __mul__(self,u):
        return Vector.__mul__(self,u)+self.z*u.z
    def __add__(self,u):
        return Vector3D(self.x+u.x,self.y+u.y,self.z+u.z)
    def __lt__(self,w):
        return abs(self)<abs(w)
    
    
if __name__=="__main__":
    v=Vector3D(2,3,-4)
    u=Vector3D(1,4,2)
    print(v)
    print(f"abs({v}) = {abs(v)}")
    print(f"-{v}={-v}")
    print(f"{v}*{u} = {v*u}")
    print(f"{v}+{u} = {v+u}")
    print(f"{v}<{u} = {v<u}")
    
