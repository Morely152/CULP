m = int(input("叫卖人数："))
import random

i = 1
n = 0

def p_add(price_0):
    """模拟叫价的函数"""
    adds = random.randint(0,9)
    if adds <= 6:
        price_0 += 10
    else:
        price_0 += 20
    print("  抽到了",adds,"价格变为",price_0)
    return price_0
    
while i <= m: 
# 游客层面的循环
    print("\n\n第",i,"位客人开始叫卖，底价为40")
    price_0 = 40 # 下一位客人叫卖时，需要初始化单价为40
    p_continue = True
    while p_continue:
    # 单个游客叫价层面的循环	
        price_0 = p_add(price_0) #　调用函数进行叫价
        if price_0 == 150:
            print("  这位客人成功买到了优质榴莲")
            n += 1
            p_continue = False
        elif price_0 >= 150:
            print("  这位客人叫卖失败")
            p_continue = False
    i += 1

p = n / m
print("\n\n一共有",m,"位客人进行叫卖，其中",n,"位叫卖成功，成交率为",p)
