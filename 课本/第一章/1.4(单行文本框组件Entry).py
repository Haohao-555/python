from tkinter import *
win=Tk();
win.title("文本框");
win.geometry("800x600");
#单行文本框
E1=Entry(win,width=20)#创建组件及大小
s=StringVar();#创建对象，以至于后面可以使用get() set()
              #get()读取文本框内容，set()输出内容
s.set("你好,世界")
E1=Entry(win,textvariable=s,state='readonly');#state='readonly'设置不能修改
E1.place(x=10,y=10);#设置组件位置
print(s.get());
win.mainloop();
