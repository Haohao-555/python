import tkinter
win=tkinter.Tk();
win.title("登录");
win.geometry("200x80");
L1=tkinter.Label(win,text="用户名：",width=6);
L1.place(x=1,y=1);
L2=tkinter.Label(win,text="密码：",width=6);
L2.place(x=1,y=20);
E1=tkinter.Entry(win,width=20);
E1.place(x=45,y=1);
E2=tkinter.Entry(win,width=20,show="哈");
E2.place(x=45,y=20);
B1=tkinter.Button(win,text="登录",width=8);
B1.place(x=40,y=40);
B2=tkinter.Button(win,text="取消",width=8);
B2.place(x=110,y=40);
win.mainloop();

#也可以看书38页例1-17.
#好处：可以精准把组件放在窗口
