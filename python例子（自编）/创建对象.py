class Car:
    price=1000
    def __init__(self,c,w):
        self.color=c
        self.__weight=w
car1=Car("红色",10.5)
car2=Car("绿色",12.4)
print(car1.color)
print(car2.color)
print(car1.__Car__weight)
print(car1.__weight)
