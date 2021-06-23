import random

b = random.randint(1,6)



corn = 5000
count = 0
while True:
    a=int(input("请输入一个随机数:"))
    if corn < 500:
        print("余额不足，此次一共猜测次数为:",count)
        break
    elif a != b:
        print("猜错了，金币扣除500")
        corn = corn -500
        count = count + 1
    elif a== b:
        print("猜对了，金币奖励1000")
        corn = corn+1000
        count = count + 1


























