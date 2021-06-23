import random

a = random.randint(0,10)
s=0
while True:
    b = int(input("请输入一个随机数:"))
    if a > b:
        print("小了")
        s=s+1
    elif a < b:
        print("大了")
        s=s+1
    else:
        print("恭喜，猜对了!! 随机数为:",b  ,"次数为",s+1)
        break