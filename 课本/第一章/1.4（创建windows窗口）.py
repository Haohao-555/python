import tkinter
win=tkinter.Tk();#创建一个窗口
win.title('我的第一个GUI程序');
win.geometry("800x600");#设置窗口的大小
#也可以：窗口对象.minsize("最小宽度x最小高度")；
#        窗口对象.maxsize("最大宽度x最大高度")；
win.mainloop();


#前两句也可以：from tkinter import *
#              win=Tk();
#后面都一样
