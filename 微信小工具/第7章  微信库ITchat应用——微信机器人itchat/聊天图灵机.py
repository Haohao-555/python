import urllib,json
from urllib import request
from urllib import parse
def getHtml(url, data):  
    page = request.urlopen(url,data)  
    html = page.read()
    html = html.decode("utf-8")  #decode()命令将网页的信息进行解码否则乱码
    return html  
if __name__ == '__main__':  
    key ='e5ccc9c7c8834ec3b08940e290ff1559'     
    #url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='+ info
    url = 'http://www.tuling123.com/openapi/api'
    while True:  
        req_info = input('我: ')
        #发给服务器数据
        query = {'key': key, 'info': req_info}
        data = parse.urlencode(query).encode('utf-8') 	#使用urlencode方法转换标准格式
            
        response = getHtml(url, data)  
        data = json.loads(response)  #字典数据
        print (data)
        print ('机器人: '+data['text'] )

        

