import turtle
turtle.bgcolor("black")
colors=["blue","yellow","green","red","pink","white"]
words=[]
word=turtle.textinput("表白","输入你想说的三个字或者点击[enter]退出:")
while word!="":
                      words.append(word)
                      word=turtle.textinput("表白","输入你想说的三个字或者点击[enter]退出:")
for x in range(100):
                                             turtle.pencolor(colors[x%Len(words)])
                                             turtle.penup()
                                             turtle.forward(x*4)
                                             turtle.pendown()
                                             turtle.write(words[x%Len(words)],font=("Arial",int((x+4)/4),"bold"))
                                             turtle.left(360/len(words)+2)
                      
