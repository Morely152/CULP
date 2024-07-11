x=int(input("请输入红包总个数（个）:"))
m=float(input("请输入红包总金额（元）:"))

i=1
import random
for i in range(1,x):
  cmax=2*m/x
  c=random.uniform(0.01,cmax)
  d=float('%.2f' % c)
  print("第",i,"个红包的金额为",d,"元")
  m=m-d
  i=i+1

d=m
e=float('%.2f' % d)
print("第",i,"个红包的金额为",e,"元")
