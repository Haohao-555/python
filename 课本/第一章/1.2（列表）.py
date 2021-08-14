#创建一维列表(并初始化)
list1=['中国','美国','日本','俄罗斯'];
print(len(list1));#计算列表长度
#查找元素
print(list1[1]);
#修改元素
list1[1]='德国'
print(list1);
#删除元素方法（1）
del list1[1];
print(list1);
#删除元素方法（2）
list1.remove('日本');
print(list1);
#删除元素方法（3）
list1.pop(1);#list1.pop()默认删除最后一个元素
print(list1);
#添加元素（列表的最后一个开始加）
list1.append('韩国');
print(list1);

#创建三维列表
rows=3;#控制维数
cols=6;#控制一个维数多少元素
list2=[[0 for col in range(cols)]for row in range(rows)];
print(list2);

#快速生成列表(1)
L=[];
L=list(range(1,10));
print(L);

#快速生成列表(2)
L=[];
for x in range(1,10):
   L.append(x*x);
print(L);

#快速生成列表(3)
L=[x*x for x in range(1,10) if x%2==0]#[计算表达式 循环表达式 条件表达式]
print(L);

#例子(大写变小写)
L=['Hello','world','IBM']
L=[s.lower() for s in L]
print(L);

#例子(随机组合)
print([m+n for m in 'ABC' for n in 'EFG']);


