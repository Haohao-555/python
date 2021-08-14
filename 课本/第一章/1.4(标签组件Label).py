from tkinter import *
win=Tk();
win.title("窗口");
L1=Label(win,text="比心",anchor='n');
L1.pack();
L2=Label(win,bitmap='questhead');
L2.pack();
bm=PhotoImage(file=r'E:\pythonwork\python项目案例开发从入门到实战\第一章\背景.png');
L3=Label(win,image=bm);
L3.bm=bm;
L3.pack();
win.mainloop();
