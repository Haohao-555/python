# 导入模块
from PIL import Image
 
# 转换函数
def convert(img):
    # 要索引的字符列表
    ascii_char = list("@@￥%&%@%@#&%@￥#￥#%*%￥#！@#￥%￥&￥#&*")
 
    # 字符长度
    length = len(ascii_char)
    # 读取图像文件
    img = Image.open(img)    
    # 获得图片的宽和高
    (width,height) = img.size
    # 对图像进行一定缩小
    img = img.resize((int(width*0.1),int(height*0.05)))
    # 转为灰度图像
    img = img.convert("L")  
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            # 获取每个坐标像素点的灰度
            gray = img.getpixel((j, i))  
            # 获取对应坐标的字符值
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)] 
        txt += '\n'
    return  txt
 
# 传入需要转换的原始图片
picture=input("请输入图片名字.后缀名(默认本地)")
txt = convert(picture)
# 把转换后的字符存入txt文件
file=input("请输入你保存的文件(默认本地)")
f = open(file+".txt","w")
f.write(txt)            
f.close()
print("转换成功")
