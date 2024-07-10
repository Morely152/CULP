#模拟座位表
stu_line0 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stu_line1 = [ 0,20,12, 1,11,19,34,15, 6,25,16, 0]
stu_line2 = [ 0, 3, 5,40,27, 2,14,29,22,39,33, 0]
stu_line3 = [ 0,24, 4,30,21, 8, 9,37,32,26,38, 0]
stu_line4 = [ 0,17,35,10,31,36,13,28, 7,23,18, 0]
stu_line5 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stu_group = [stu_line0,stu_line1,stu_line2,stu_line3,stu_line4,stu_line5]

#准备
import random
student = {}
m = 0

#函数部分
def select_stu():
    """随机取值取向"""
    stu_num = random.randint(1,40)
    stu_dir = random.randint(1,4)
    if stu_dir ==1:
        s_direction = "左边"
    if stu_dir ==2:
        s_direction = "右边"
    if stu_dir ==3:
        s_direction = "前面"
    if stu_dir ==4:
        s_direction = "后面"
    student["number"] = stu_num
    student["direction"] = s_direction
    print("•",stu_num,"号的",s_direction)

def stu_position():
    """定位找值"""
    if student["number"] in stu_line1:
        stu_line = stu_line1
        pos_x = 1
    if student["number"] in stu_line2:
        stu_line = stu_line2
        pos_x = 2
    if student["number"] in stu_line3:
        stu_line = stu_line3
        pos_x = 3
    if student["number"] in stu_line4:
        stu_line = stu_line4
        pos_x = 4
    student["x"] = pos_x
    student["y"] = stu_line.index(student["number"])
    """按向找值"""
    if student["direction"] == "左边":
        next_student = stu_line[student["y"] - 1]
    if student["direction"] == "右边":
        next_student = stu_line[student["y"] + 1]
    if student["direction"] == "前面":
        next_studen_line = stu_group[student["x"] - 1]
        next_student = next_studen_line[student["y"]]
    if student["direction"] == "后面":
        next_studen_line = stu_group[student["x"] + 1]
        next_student = next_studen_line[student["y"]]
    #防止边界取向
    if next_student == 0:
        next_student = student["number"]
    student["number"] = next_student

def next_stu():
    """抽取下一个值"""
    selected_list = list(str(student["number"]))
    end_number =selected_list[-1]
    a = int(end_number)
    next_list = [a,a+10,a+20,a+30]
    index = random.randint(0,3)
    next_number = next_list[index]
    while next_number == student["number"]:
        index = random.randint(0,3)
        next_number = next_list[index]
    """抽取下一个方向"""
    next_direction = random.randint(1,4)
    if next_direction == 1:
        s_direction = "左边"
    if next_direction == 2:
        s_direction = "右边"
    if next_direction == 3:
        s_direction = "前面"
    if next_direction == 4:
        s_direction = "后面"
    student["number"] = next_number
    student["direction"] = s_direction
    print("•",next_number,"号的",s_direction)

#循环部分
stu_amount = int(input("Number of student:"))
if stu_amount < 1:
    print("学生人数应大于零！")
else:
    #抽取第一个学生
    select_stu()
    stu_position()
    print("  即",student["number"],"号")
    m += 1
    #抽取其余学生
    while m < stu_amount:
        next_stu()
        stu_position()
        print("  即",student["number"],"号")
        m += 1
        




















