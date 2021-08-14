class Person:
    num=1
    def __init__(self, str,n):
       self.name=str
       self.age=n
    def SayHello(self):
        print("Hello!")
    def PrintName(self):
        print("姓名:",self.name, "年龄:",self.age)
    def PrintNum(Person):
        print(Person.num)
p1=Person("黄佳浩",21)
p2=Person("黄佳佳",18)
p1.SayHello()
p1.PrintName()
p2.PrintName()
Person.num=2
p1.SayHello()
p1.PrintNum()
p2.PrintNum()
