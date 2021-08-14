import time
import pygame
#音乐路径
filePath=r'E:\pythonwork\音乐播放器\音乐\筷子兄弟 - 父亲.mp3'
#初始化
pygame.mixer.init();
#加载音乐
pygame.mixer.music.load(filePath);
#播放
pygame.mixer.music.play();
#设置播放时间
time.sleep(10);
