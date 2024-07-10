import random # 用于生成随机数
import time   # 用于让程序暂停一段时间

# 初始化各位玩家的属性
player_0 = {"hp":1, "p_ch0":0, "p_kill":60}
player_1 = {"hp":1, "p_ch0":10, "p_kill":50}
player_2 = {"hp":1, "p_ch0":15, "p_kill":45}
player_3 = {"hp":1, "p_ch0":20, "p_kill":40}
player_4 = {"hp":1, "p_ch0":25, "p_kill":35}
player_5 = {"hp":1, "p_ch0":30, "p_kill":30}
player_6 = {"hp":1, "p_ch0":35, "p_kill":25}
player_7 = {"hp":1, "p_ch0":40, "p_kill":20}
player_8 = {"hp":1, "p_ch0":45, "p_kill":15}
player_9 = {"hp":1, "p_ch0":50, "p_kill":10}

# 定义玩家列表，方便后续处理
players = [player_0,player_1,player_2,player_3,player_4,player_5,player_6,player_7,player_8,player_9]

# 初始化计数变量
i = 1

def p_judge(p):
    """依据概率判断事件是否发生"""
    p_rand = random.randint(0,100)
    if p_rand <= p:  # 发生
        return 1
    else:           # 不发生
        return 0

# 游戏主循环
while player_0["hp"] == 1:
    print("\n\n第",i,"轮：")

    while True:                                # 玩家0指定目标
        target = int(input("    选择目标："))

        # 判断玩家输入是否合法
        if target < 1 or target >9:
            print("    请在1-9号之间选择。")
        elif players[target]["hp"] == 0:
            print("    该玩家已经被淘汰了。")
        else:
            break

    if p_judge(player_0["p_kill"]) == 0:       # 判断玩家是否击中目标
        print("    哦豁，没有击中目标…")
    else:
        print("    成功击中",target,"号。")
        players[target]["hp"] = 0
       
    for player in players[1:10]:                # 其他玩家射击
        if player["hp"] == 1:  # 跳过淘汰的玩家
            print("\n    ",players.index(player),"号开始射击：")
            time.sleep(1)

            if p_judge(player["p_ch0"]) == 1:  # 判断是否击中玩家0(导致游戏结束)
                print("    他向你瞄准了！")
                time.sleep(1)

                if p_judge(player["p_kill"]) == 0:
                    print("    Fortunately,他没有击中你。")
                    time.sleep(1)
                else:
                    print("    你被击中啦！游戏结束。")
                    exit(0)
            
            else:
                while True:
                    target = players[random.randint(1,9)]
                    if target["hp"] == 1 and target != player:
                        print("    他瞄准了",players.index(target),"号")
                        time.sleep(1)
                        break
                if p_judge(player["p_kill"]) == 0:
                    print("    但他没有击中。")
                    time.sleep(1)
                else:
                    print("    他击中了",players.index(target),"号")
                    time.sleep(1)
                    players[players.index(target)]["hp"] = 0
                    
    print("\n结算情况：")                           # 每轮之后，输出结算情况
    time.sleep(1)
    m = 0                   # 初始化记取淘汰玩家数的变量
    print("    1  2  3  4  5  6  7  8  9  ")
    print("    ",end = "")  # 输出空格以与上方对齐
    for player in players[1:10]:
        if player["hp"] == 1:
            print("V",end = "  ")
        else:
            print("X",end = "  ")
            m += 1
    print("\n    一共有",m,"人淘汰。")
    time.sleep(1)

    if m == 9:
        print("\n\n恭喜获胜！")
        exit(0)

    i += 1