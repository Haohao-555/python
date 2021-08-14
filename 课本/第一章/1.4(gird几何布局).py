from tkinter import *
win=Tk();
win.title('Grid几何布局');
win.geometry("200x200");
L1=Button(win,text='1',width=7,bg='yellow');
L2=Button(win,text='2',width=7);
L3=Button(win,text='3',width=7);
L4=Button(win,text='4',width=7);
L5=Button(win,text='5',width=7,bg='green');
L6=Button(win,text='6',width=7);
L7=Button(win,text='7',width=7);
L8=Button(win,text='8',width=7);
L9=Button(win,text='9',width=7,bg='yellow',fg='green');#按钮为黄色,字体9为绿色
L0=Button(win,text='0');
Lp=Button(win,text='.');
L1.grid(row=0,column=0);#按钮放置在0行0列
L2.grid(row=0,column=1);
L3.grid(row=0,column=2);
L4.grid(row=1,column=0);
L5.grid(row=1,column=1);
L6.grid(row=1,column=2);
L7.grid(row=2,column=0);
L8.grid(row=2,column=1);
L9.grid(row=2,column=2);
L0.grid(row=3,column=0,columnspan=2,sticky=E+W);#跨两列，sticky=E+W(左右贴紧)
Lp.grid(row=3,column=2,sticky=E+W);

win.mainloop();
