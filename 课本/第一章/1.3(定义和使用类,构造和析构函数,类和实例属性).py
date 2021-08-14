#类的定义：成员属性和成员方法统称为类的成员。对象是类的具体实例，类是对象的抽象

#对象的创建：对象名=类名（）

#构造函数：_ _init_ _() 一般用于完成对象数据成员设置初值或进行其他必要的初始化工作
#析构函数：_ _del_ _() 用来释放对象占用的资源
#用户如果没有涉及析构函数和构造函数，系统会提供默认的析构函数和构造函数（构造函数基本会用到）

#类属性和实例属性
class Person:
    num=1;#类属性（在类的内部，构造函数外部）所有类的对象都可以使用
    def __init__(self,str,n):#类的所有实例方法都必须至少有一个名为"self"的参数，并且必须是方法的第一个形参。
        #"self"参数代表将来要创建的对象本身
        self.name=str;#实例属性（必须在构造函数）
        self.age=n;
    def SayHello(self):
        print("Hello");
    def PrintName(self):
        print("姓名",self.name,"年龄",self.age);#访问实例属性：对象名.属性名
    def PrintNum(self):
        print(Person.num);#访问类属性: 类名.属性名 或 对象名.属性名
#主程序
p1=Person("小明",30);
p2=Person("小红",20);
p1.PrintName();#访问方法：对象名.方法名（形参）
p2.PrintName();
Person.num=2;
p1.PrintNum();
p2.PrintNum();
a=isinstance(p1,Person);#判断对象是否为某个类的实例
print(a);

