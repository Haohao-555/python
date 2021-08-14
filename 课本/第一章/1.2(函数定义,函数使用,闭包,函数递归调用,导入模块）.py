#(1)函数定义
def printHello():
    print('hello');
printHello();   
#def 函数名(函数参数)
   #函数体
   #return 表达式或值

#可以不用指定返回值类型（变量都是弱类型，python会自动根据值来维护其类型）
#要先定义函数才能使用函数
#python可以返回多个值（具体看判断字符大小的个数）

x=2;#全局变量
def fun1():
    print(x,end=" ");
def fun2():
    g=2;#局部变量
    global x;#在函数内部改变全局变量必须使用global关键字
    a=x+1;
    print(a,end=" ");
fun1();
fun2();

#闭关（函数嵌套）python特有（在一个函数里面再次定义一个函数）
#函数的递归调用（具体看计算阶乘）
#模块 关键字import
#（1）导入模块：import 模块名（等价于form math import *）
#（2）使用函数名：模块名.函数名
#(3)导入模块特定一个函数：from 模块名 import 函数名  则使用函数名时直接写函数名就好
