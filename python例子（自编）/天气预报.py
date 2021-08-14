import urllib, urllib2, sys
import ssl


host = 'https://tianqimore.market.alicloudapi.com'
path = '/weather'
method = 'POST'
appcode = 'aafa8504cb9a41e79c7ed194d9806b60'
querys = ''
bodys = {}
url = host + path

bodys['month'] = '''201907'''
bodys['src'] = '''hebei'''
bodys['type'] = '''1'''
post_data = urllib.urlencode(bodys)
request = urllib2.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)
