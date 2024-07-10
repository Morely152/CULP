print("python解鸡兔同笼")  

  #获取头和脚的总数
h=int(input("请输入头的总数"))
f=int(input("请输入脚的总数"))

  #验证数值是否可进行计算
if h<1:
    print("NumericError:头的总数应为正整数")
elif f<2*h:
    print("NumericError:脚的总数应大于等于头的总数的两倍")
elif f>4*h:
    print("NumericError:脚的总数应小于等于头的总数的四倍")
elif f%2!=0:
    print("NumericError:脚的总数应该为偶数")
else:
  #进行运算
    r=f/2-h
    c=2*h-f/2
  
  #输出鸡和兔的数量
print("鸡有","%d"%c,"只")
print("兔有","%d"%r,"只")
























