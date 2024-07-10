print("BMI计算")
h=float(input("请输入身高（m）"))
w=float(input("请输入体重（kg）"))

BMI=w/(h**2)
print("BMI指数为：",BMI)
print("根据BMI显示，你的状况为：")

if BMI<=18.5:
    print("偏瘦")
elif BMI<=23.9:
    print("正常")
else:
    print("偏胖")