import pygame
import tkinter
from tkinter import *
from tkinter import filedialog
def pause():
    pygame.mixer.music.pause();
    
def stop():
    pygame.mixer.music.stop();
    
def start():
    pygame.mixer.music.unpause();
    
def choose():
    file=filedialog.askopenfilename();
    pygame.mixer.music.load(file);
    pygame.mixer.music.play();
    
win=tkinter.Tk();
win.title("播放器");
win.geometry("400x300+400+200");
one=Menu();
win.config(menu=one)
Menu(one);
pygame.init();
Label(win,text="欢迎使用播放器").pack();
Button(win,text="选择音乐",command=choose).pack();
Button(win,text="暂停音乐",command=pause).pack();
Button(win,text="继续播放",command=start).pack();
Button(win,text="停止音乐",command=stop).pack();
win.mainloop();



