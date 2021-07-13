breadNum = 0
clientMon = 30
from threading import Thread
import time

class cooker(Thread):

    cookerName = ""

    def run(self) -> None:
        global breadNum
        global clientMon
        while True:
            if breadNum < 500:    #厨师做面包
                breadNum = breadNum + 1
                print(self.cookerName,"扔进篮子一个面包，面包有",breadNum,"个！")
            elif breadNum == 0:      #篮子空了
                print("篮子里没有面包了，请等一会儿！！！")
                time.sleep(0.1)
            elif breadNum >= 500:  # 篮子满了
                print("篮子里面装不下了，请等一会儿！！！")
                time.sleep(0.1)
                if  clientMon < 3:
                    break
class customer(Thread):
    clientName = ""
    purQuan = 0  # 购买数量

    def run(self) -> None:
        global breadNum
        global clientMon
        while True:
            if breadNum > 0 and clientMon > 3:  # 顾客买面包
                breadNum = breadNum - 1
                print(self.clientName, "购买了一个面包还有", clientMon)
                clientMon = clientMon - 3
                self.purQuan = self.purQuan + 1
            elif clientMon < 3:                        #没钱买面包
                    print(self.clientName,"的金币已花光，买了",self.purQuan,"个面包")
                    break
'''            elif breadNum == 500 and self.clientMon < 3:
                break'''

c1 = cooker()
c2 = cooker()
c3 = cooker()

cu1 = customer()
cu2 = customer()
cu3 = customer()
cu4 = customer()
cu5 = customer()
cu6 = customer()

c1.cookerName = "小离"
c2.cookerName = "小虎"
c3.cookerName = "小王"
cu1.clientName = "天灵"
cu2.clientName = "妄图"
cu3.clientName = "龙利"
cu4.clientName = "屠星"
cu5.clientName = "费遂"
cu6.clientName = "离厝"


c1.start()
c2.start()
c3.start()
cu1.start()
cu2.start()
cu3.start()
cu4.start()
cu5.start()
cu6.start()





















































