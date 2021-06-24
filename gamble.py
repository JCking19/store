import random

b = random.randint(1,6)

corn = 5000
count = 0
right = 0
while True:
    a=int(input("请输入一个随机数:"))
    if corn < 500:
        print("余额不足，此次一共猜测次数为:",count+1,"猜对次数为",right)
        break
    elif a != b:
        if a > b:
            print("猜的数字大了")
        elif a < b:
            print("猜的数字小了")
        print("猜错了，金币扣除500")
        corn = corn - 500
        count = count + 1
    elif a == b:
        print("猜对了，金币奖励1000，数字为",a)
        corn = corn+1000
        count = count + 1
        right = right + 1
        b = random.randint(1,6)

























