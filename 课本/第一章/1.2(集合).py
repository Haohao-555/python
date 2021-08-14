#创建集合（无序不重复元素）作用：进行成员关系测试和删除重复集合
student={'Jack','Jim','Marry','Tom','Jack'}
print(student);
a=set('Jackkac')#单个字符，创建空集合只能用set();
print(a);

#成员测试
if('Rose'in student):
    print('Rose在集合中');
else:
     print('Rose不在集合中');

#集合运算
a=set('abcd');
b=set('cdef');
print("a与b的差集",a-b);
print("a与b的并集",a|b);
print("a与b的交集",a&b);
print("a和b中不同时存在的元素：",a^b);
