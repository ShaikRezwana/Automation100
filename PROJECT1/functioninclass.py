class A():
    def __init__(self,a,b):
        print("this is constructor")
        c=a+b
        print(c)
    def hello(self):
        print("hello world")
    def sum(self,a,b):
        c=a+b
        print(c)
    def mul(self,a,b):
        c=a*b
        return c
obj=A(34,56)
obj.hello()
obj.sum(10,100)
x=obj.mul(10,20)
print(x)
