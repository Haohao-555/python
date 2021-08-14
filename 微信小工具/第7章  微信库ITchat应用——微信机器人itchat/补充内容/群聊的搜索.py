import requests
import json
import itchat
from itchat.content import *
itchat.auto_login()
df = itchat.search_chatrooms(name=u'夏家')
print(df)
df = itchat.search_chatrooms(userName='@f47fcf4533413b5fad998e30459a86866623c68cb6a363c7aeff208ec03fbb8d')
print(df)
itchat.run()
