import os

os.chdir(r"E:\Python_Automation\advanced python OOP")

class Vector:
    def __init__(self, x, y):
        self.X=x
        self.Y=y
    def __add__(self,other):
        return Vector(self.X+other.X,self.Y+other.Y)
    def __repr__(self): # = to_string dunder method
        return f'X: {self.X}, Y: {self.Y}'
    # def pr():
    #     print(f'X: {self.X}, Y: {self.Y}')
    def __call__(self):
        print(f"Hello! I was called")
    def __len__(self):
        return 10

v1=Vector(10,20)
v2=Vector(20,30)
v3=v1+v2
print(v1)
print(v2)
print(v3)
v3()
