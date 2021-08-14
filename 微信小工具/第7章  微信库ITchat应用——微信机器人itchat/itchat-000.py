# 加载包
import itchat
# 登陆
itchat.auto_login(picDir='test.png')
# 发送文本消息，发送目标是“文件传输助手”
itchat.send('Hello, filehelper', toUserName='文件传输助手')


##import itchat
##
##@itchat.msg_register(itchat.content.TEXT)
##def print_content(msg): 
##    print(msg['Text'])
##
##itchat.auto_login(enableCmdQR=True)
##itchat.run()
