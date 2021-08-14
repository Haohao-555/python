#私有属性：用_ _开头的表示为私有属性，否则为公有属性
#私有属性在类的外部不能被直接访问 (1)需要通过调用对象的公有成员方法来访问 
#                                 (2）在外部通过Python支持的特殊方法来调用
class Car:
    def __init__(self,c,w):
        self.color=c;#公有属性
        self.__weight=w;#私有属性
    def PrintWeight(self):
        return self.__weight;#访问私有属性
#主程序
car1=Car("Red",10.5);
car2=Car("Blue",90);
print(car1.color);
print(car1._Car__weight);#(2)对象名._类名_ _私有属性（不建议在类的外部使用）
print(car1.PrintWeight());#(1)


#私有属性是为了数据封装和保密而设的属性，一般只能在类的成员方法（类的内部）中使用
#公有属性是可以公开使用的，既可以在类的外部使用也可以在内部
