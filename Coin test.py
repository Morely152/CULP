m=int(input("请输入试验次数"))

import random
i=0
h=0

for f in range(1,m+2):
    c=random.randint(0,1)

    if c==0:
        print("第",i,"次硬币为反面朝上")
        i=i+1
    elif c==1:
        print("第",i,"次硬币为正面朝上")
        h=h+1
        i=i+1
    
p=h/m
print("经过",m,"次试验，硬币正面朝上的次数为",h,"次，概率为：",p)
