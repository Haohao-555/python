#父类
class Animal:
    def run(self):
        print("Animal is running");
#子类
class Cat(Animal):
    def run(self):
        print("Car is running");#方法重写
cat1=Cat();
cat1.run();#执行方法重写的内容
