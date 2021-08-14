import tkinter
win=tkinter.Tk();#创建一个窗口
win.title('pack几何布局');
win.geometry("800x600");#设置窗口的大小


labe1=tkinter.Label(win,text='hello,python');#创建Label组件
labe1.pack();#组件label的位置设置书40-41页图1-10    

button1=tkinter.Button(win,text='BUTTON1');#创建Button组件
button1.pack(side=tkinter.LEFT);#将button1组件添加到窗口中显示,左停靠

button2=tkinter.Button(win,text='BUTTON2');
button2.pack(side=tkinter.RIGHT);#将button2组件添加到窗口中显示,右停靠（默认正中间）
win.mainloop();
