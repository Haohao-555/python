#方法：公有方法，私有方法（以_ _开始），静态方法 （前两者为对象方法，后者为类方法）
#私有方法不能通过对象名直接调用。（1）只能在属于对象方法（公有方法）中通过self调用
#                                （2）在外部通过Python支持的特殊方法来调用

class Fruit:
    price=0
    def __init__(self):
        self.__color="Red";#私有属性
        self.__city="Kunming";
        
    def __outputColor(self):#私有方法
        print(self.__color);
        
    def __outputCity(self):
        print(self.__city);
        
    def output(self):#公有方法（1）
        self.__outputColor();#调用私有方法
        self.__outputCity();
        
    @staticmethod#可写可不写（主要是与公有方法做区别）
    def getPrice():#静态方法
        return Fruit.price;
    
    @staticmethod
    def setPrice(p):
        Fruit.price=p;
#主程序
apple=Fruit();
apple.output();
print(Fruit.getPrice())
Fruit.setPrice(9);
print(Fruit.getPrice())#也可以 apple.getPrice()
apple._Fruit__outputColor();#(2)对象名._类名_ _私有方法
