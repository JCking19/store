import random

marketPro = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13]
]

coupon = [
    ["机械革命",15000*70/100],
    ["HUAWEI watch",1200*90/100],
    ["MAC PC",13000*80/100],
    ["Iphone 54 plus",45000*98/100],
    ["辣条",2.5*70/100],
    ["老干妈",13*85/100]
]

print("***********欢迎来到JCkingMarket***************")
coup = int(input("先进行优惠券抽奖:（输入1进行抽奖，输入2退出抽奖环节）:"))
while range(1):
    if coup == 1:
        c = random.randint(0,len(coupon)-1)
        print("恭喜您抽中",coupon[c])
        break
#新知识:枚举类型直接显示全部 enum
# .isdigit() 是否能被看成数字：
#随机的优惠券名
#print(coupon[c][0])

#娱乐区只能进入一次
print("*************************************************")
area = int(input("请选择进去那个区域:(输入1进入娱乐区，输入2进入购物区)"))
print("*************************************************")
print("*****************欢迎来到娱乐区*******************")
while True:
    if area == 1:
        b = random.randint(1, 6)

        corn = 5000
        count = 0
        right = 0
        while True:
            a = int(input("请输入一个随机数:"))
            if corn < 500:
                print("余额不足，此次一共猜测次数为:", count + 1, "猜对次数为", right)
                break
            elif a > 50:
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
                print("猜对了，金币奖励1000，数字为", a)
                corn = corn + 1000
                count = count + 1
                right = right + 1
                b = random.randint(1, 6)
        break

    elif area == 2:
        break
    else:
        print("请输入正确的选项！！！！")

print("*************************************************")
print("*****************欢迎来到购物区*******************")

money = int(input("请输入您的预算余额:"))

myTrolley = []

while True:
    for index,value in enumerate(marketPro):
        print(index,"\t\t",value)
    product = input("请输入您要买的商品：")

    if product.isdigit():
        product = int(product)
        if product > len(marketPro) - 1:
            print("您要的商品不存在！")
        elif product < 0:
            print("您要的商品不存在！")
        else:
            if money >= marketPro[product][1]:
                myTrolley.append(marketPro[product])
                money = money - marketPro[product][1]
                print("成功添加商品:",marketPro[product][0],"预算剩余: ￥",money)
            else:
                print("对不起，您的预算不足")
                #补充预算的逻辑
    elif product == 'q' or product == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！")


print("请选择是否使用优惠券:(1为使用,2为不使用)")
d = int(input())
while True:
   if d == 1:
       print("下面是您的购物小条，请拿好：")
       for index, value in enumerate(myTrolley):
        #未执行到下一步
          print(value[0],coupon[c][0])
          print(value[1],coupon[c][1])
          if coupon[c][0] == value[0]:
              value[1] == coupon[c][1]
          print(index+1, "   ", value)
          continue
       print("您的钱包还剩：￥", money)
       break


   elif d == 2:
       print("下面是您的购物小条，请拿好：")
       for index, value in enumerate(myTrolley):
           print(index+1, "   ", value)
       print("您的钱包还剩：￥", money)
       break














































