import requests #首先导入库
import  re
#设置默认配置
MaxSearchPage = 20 # 收索页数
CurrentPage = 0 # 当前正在搜索的页数
DefaultPath = "pricture11" # 默认储存位置
NeedSave = 0 # 是否需要储存
#图片链接正则和下一页的链接正则
def imageFiler(content): # 通过正则获取当前页面的图片地址数组
          return re.findall('"objURL":"(.*?)"',content,re.S)
def nextSource(content): # 通过正则获取下一页的网址
          next = re.findall('<div id="page">.*<a href="(.*?)" class="n">',content,re.S)[1]
          print("---------" + "http://image.baidu.com" + next) 
          return next
#爬虫主体
def spidler(source):
          content = requests.get(source,allow_redirects=False).text  # 通过链接获取内容
          imageArr = imageFiler(content) # 获取图片数组
          global CurrentPage
          print("Current page:" + str(CurrentPage) + "**********************************")
          for imageUrl in imageArr:
              print(imageUrl)
              global  NeedSave
              if NeedSave:  			# 如果需要保存图片则下载图片，否则不下载图片
                 global DefaultPath
                 try:
                      # 下载图片并设置超时时间,如果图片地址错误就不继续等待了
                      picture = requests.get(imageUrl,timeout=10) 
                 except:                
                      print("Download image error! errorUrl:" + imageUrl)   
                      continue
                 # 创建图片保存的路径
                 imageUrl = imageUrl.replace('/','').replace(':','').replace('?','')
                 pictureSavePath = DefaultPath + imageUrl
                 fp = open(pictureSavePath,'wb') # 以写入二进制的方式打开文件
                 fp.write(picture.content)
                 fp.close()
          global MaxSearchPage
          if CurrentPage <= MaxSearchPage:    #继续下一页爬取
               if nextSource(content):
                   CurrentPage += 1 
                   # 爬取完毕后通过下一页地址继续爬取
                   spidler("http://image.baidu.com" + nextSource(content)) 
#爬虫的开启方法
def  beginSearch(page=1,save=0,savePath="pricture11/"): 
          # (page:爬取页数,save:是否储存,savePath:默认储存路径)
          global MaxSearchPage,NeedSave,DefaultPath
          MaxSearchPage = page
          NeedSave = save					#是否保存，值0不保存，1保存
          DefaultPath = savePath				#图片保存的位置
          key = input("请输入你要查找的关键字图片：")
          
          StartSource = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + str(key) + "&ct=201326592&v=flip" #分析链接可以得到,替换其`word`值后面的数据来搜索关键词
#         
          spidler(StartSource)
#调用开启的方法就可以通过关键词搜索图片了
beginSearch(page=5,save=1)			# page=5是下载前5页，save=1保存图片
