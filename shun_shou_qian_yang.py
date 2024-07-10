# -*- coding: utf-8 -*-

# 介绍游戏规则
print('''欢迎试玩Python小游戏"顺手牵羊"(v.beta)！
·在游戏中，你将扮演一位猎人捕捉草地上的一只羊，
·规则很简单，移动"我"到达"羊"的左边，即可成功抓住淘气的小羊！
·移动时，你可以从"上下左右"中选择一个方向，在1～3中选择一个速度，
 ·比如"向左移动2格"可表示为"左2"。''')

start_game = str(input("\r有兴趣玩这个游戏吗？（输入start开始）"))
if start_game == "start":
    start = True # while循环的标志
else:
    print("不好玩吗？感谢反馈。")
    exit(0)

#准备地图，初始化猎人和羊的位置
game_map = [["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],
            ["口","口","口","口","口","口","口","口","口"],]
import math
import random
n = 0
hunter = {"x":4,"y":4}
sheep = {}
sheep["x"] = random.randint(0,8)
sheep["y"] = random.randint(0,8)
# 防止猎人和羊的初始位置相同
while sheep["x"] == 4 and sheep["y"] == 4:
    sheep["x"] = random.randint(0,8)
    sheep["y"] = random.randint(0,8)
game_map[sheep["x"]][sheep["y"]] = "羊"
game_map[4][4] = "我"

#函数部分
def print_map():
    """绘制地图"""
    print("地图如下：")
    for x in game_map:
        pos_y = 0
        for y in x:
            pos_y += 1
            if pos_y == 9:
                print(y)
            else:
                print(y,end="")

def move_sheep():
    """移动羊"""
    direction = random.randint(1,4)
    game_map[sheep["x"]][sheep["y"]] = "口"
    if direction == 1:
        direction = "左边"
        sheep["y2"] = sheep["y"] - 1
        sheep["x2"] = sheep["x"]
    if direction == 2:
        direction = "右边"
        sheep["y2"] = sheep["y"] + 1
        sheep["x2"] = sheep["x"]
    if direction == 3:
        direction = "上面"
        sheep["y2"] = sheep["y"]
        sheep["x2"] = sheep["x"] - 1
    if direction == 4:
        direction = "下面"
        sheep["y2"] = sheep["y"]
        sheep["x2"] = sheep["x"] + 1
    sheep["direction"] = direction

def sheep_position_judge():
    """检查羊的位置是否正确"""
    # 防止羊跑出地图
    while sheep["x2"] == hunter["x"] and sheep["y2"] == hunter["y"]:
        move_sheep()
    if sheep["x"] == 8 and sheep["direction"] == "下面":
        sheep["x2"] = 0
    if sheep["y"] == 8 and sheep["direction"] == "右边":
        sheep["y2"] = 0
    # 检查完毕，更新羊的位置
    sheep["x"] = sheep["x2"]
    sheep["y"] = sheep["y2"]
    game_map[sheep["x2"]][sheep["y2"]] = "羊"
    print("羊向%s处移动一格，坐标为(%s,%s)。" %(sheep["direction"],sheep["y"]+1,sheep["x"]+1))

def move_hunter():
    """移动猎人"""
    next_step = str(input("\n下一步怎么走？"))
    next_step_list = list(next_step)
    direction = next_step_list[0]
    speed = int(next_step_list[1])
    if direction == "左":
        hunter["x2"] = hunter["x"]
        hunter["y2"] = hunter["y"] - speed
    if direction == "右":
        hunter["x2"] = hunter["x"]
        hunter["y2"] = hunter["y"] + speed
    if direction == "上":
        hunter["x2"] = hunter["x"] - speed
        hunter["y2"] = hunter["y"]
    if direction == "下":
        hunter["x2"] = hunter["x"] + speed
        hunter["y2"] = hunter["y"]
    hunter["speed"] = speed
    game_map[hunter["x"]][hunter["y"]] = "口"   
    
def hunter_position_judge():
    """检查猎人的位置是否正确"""
    # 检查速度
    while hunter["speed"] < 0:
        print("还带挂倒档的？不可以这么走！")
        move_hunter()
    while hunter["speed"] == 0:
        print("一动不动是王八？不可以这么走！")
        move_hunter()
    while hunter["speed"] > 3:
        print("超速是要罚款的！不可以这么走！")
        move_hunter()
    # 检查位置
    while hunter["x2"] == sheep["x"] and hunter["y2"] == sheep["y"]:
        print("你踩到羊了！不可以这么走！")
        move_hunter()
    while hunter["x2"] < 0 or hunter["x2"] > 8:
        print("你出图啦！不可以这么走！")
        move_hunter()
    while hunter["y2"] < 0 or hunter["y2"] > 8:
        print("你出图啦！不可以这么走！")
        move_hunter()
        # 检查完毕，更新猎人的位置
    hunter["x"] = hunter["x2"]
    hunter["y"] = hunter["y2"]
    game_map[hunter["x2"]][hunter["y2"]] = "我"


# 游戏循环部分
# 开场
print_map()
distance = math.sqrt((sheep["x"]-4)**2 + (sheep["y"]-4)**2)
print("羊在(%s,%s)处，距离你%.2f格" %(sheep["y"]+1,sheep["x"]+1,distance))
# 循环
while start:
    move_hunter()
    n += 1
    hunter_position_judge()
    if game_map[sheep["x"]][sheep["y"]-1] == "我":
        start = False
        print_map()
        print('成功“顺手牵羊”！得分:%s' %(100 - n))
    else:
        move_sheep()
        sheep_position_judge()
        print_map()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






