import qrcode
text=input("请输入你要说的内容:");
img=qrcode.make(text);
savePath="MyCode.png";
img.save(savePath);
print("二维码已经生成");
