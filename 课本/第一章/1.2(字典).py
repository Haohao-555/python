#创建字典（键是唯一的，对应值可以多个）多个键会覆盖 
#键只能是字符串，元组，数字 不能是列表
dict={'Name':'王海','Age':17,'Class':'计算机9班'}
dict1={'Name':'王海','Age':17,'Class':'计算机9班'}
dict2={'Name':'王海','Age':17,'Class':'计算机9班'}

#访问
print(dict['Name']);#如果没有该键则输出错误信息

#更新键的值
dict['Name']='王静';
print(dict['Name']);

#增加键
dict['School']='中山大学南方学院';
print(dict['School']);

#删除键的值
del dict['Name'];
print(dict);#输出内容跟初始化的一模一样
#print(dict['Name']);如果字典的键里没有数据输出会报错

#清空字典的所有元素
dict1.clear();

#删除整个字典
del dict2;

#in运算(判断某个键是否存在，不适合在判断value值上)
print('Name'in dict);
print('Age' in dict);

#获取字典中的所有值
print(dict.values());

#打印每对key和value
for key,value in dict.items():
    print(key,value);


#字典打印出来的顺序与创建之初的顺序不同的（字典是无序的，列表是有序）。
#字典不是按位置查数据的，因此在存储元素时可以进行优化。    
    
