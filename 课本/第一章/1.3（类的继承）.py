#父类
import types
class Person(object):#父类必须继承于object，否则在子类中将无法使用super()函数
    def __init__(self,name='',age=20,sex=''):
        self.setName(name);
        self.setAge(age);
        self.setSex(sex);
    def setName(self,name):
        if type(name)!=str: #内置函数type()返回被测对象的数据类型
            print("姓名必须是字符串");
            return
        self.__name=name
    def setAge(self,age):
        if type(age)!=int:
            print("年龄必须是整型");
            return
        self.__age=age;
    def setSex(self,sex):
        if sex!='男'and sex!='女':
            print("性别输入错误")
            return
        self.__sex=sex;
    def show(self):
        print("姓名",self.__name,"年龄", self.__age,"性别",self.__sex);
#子类，在其中增加一个入学年份私有属性
class Student(Person):
    def __init__(self,name='',age=20,sex='',schoolyear=2016):#子类的构造函数
        super(Student,self).__init__(name,age,sex);#调用父类的构造函数，系统不会自动调用的
        #Person.__init__(self,name,age,sex)  也可以这样
        self.setSchoolyear(schoolyear);
        
    def setSchoolyear(self,schoolyear):
        self.__schoolyear=schoolyear;
        
    def show(self):
        Person.show(self);#调用父类show()的方法,且需要带上self参数变量
        #super(Student,self).show();  也可以这样
        print("入学年份：", self.__schoolyear);
#主程序
if __name__=='__main__':
    zhangsan=Person('张三',19,'男');
    zhangsan.show();
    lisi=Student('李四',18,'女',2015);
    lisi.show();
    lisi.setAge(20);
    lisi.show();


#Python总是先查找对应类型的方法，如果不能在子类中找到相应的方法，它才开始到父类中找。
        
