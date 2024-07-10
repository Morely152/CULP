# -*- coding: utf-8 -*-
print("现在由我给出一个一到一百以内的整数，")
print("而你需要把它猜出来。")
print("想玩这个游戏吗？（输入start开始游戏）")

start_or_not=input()
if start_or_not != "start":
    print("让你玩你还不玩，给你脸了")
else:
    start = True
    import random
    unknown_number=random.randint(1,100)
    
while start:
    guessed_number=int(input("猜猜这个数是几："))
    
    if guessed_number > unknown_number:
        print("太大了，再试试吧：")
    elif guessed_number < unknown_number:
        print("太小了，再试试吧：")
    else:
        print("猜对啦！你真棒！")
        play_or_not=input("想要再玩一次吗?（输入play再次开始,输入quilt退出）")
        if play_or_not =="play":
            unknown_number=random.randint(1,100)
        elif play_or_not == "quilt":
            break
    






