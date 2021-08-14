def fac(n):
   if n==1:
       p=1
   else:
       p=(fac(n-1)*n)
   return p
a=int(input("请输入正整数:"))
print(fac(a))
