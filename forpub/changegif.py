import random

def rd():
    lsGiftIn = {'Jack':'apple', 'June':'ball', 'Mary':'card', 'Duke':'doll', 'James':'egg',
                'Tina':'flute', 'Tom':'coffee'}  # 存储参与者的姓名和自己带来的礼物
    lsGiftOut = {}  # 存储交换后的结果
    n = len(lsGiftIn)  # 参与人数
    gifts = [lsGiftIn[i] for i in lsGiftIn.keys()]  # 未分配出去的礼物
    name=[i for i in lsGiftIn.keys()]
    mygg=[lsGiftIn[a] for a in lsGiftIn.keys()]
    for x in range(n):
        flag = 0
        person = name[x]
        myGift = mygg[x]
        if myGift in gifts:
            flag = 1
            gifts.remove(myGift)
        if len(gifts)==0:
            changname = [b for b in lsGiftOut.keys()]
            na=random.choice(changname)
            gif=lsGiftOut[na]
            lsGiftOut.pop(na)
            lsGiftOut[person] = gif
            lsGiftOut[na] = myGift
        else:
            getGift = random.choice(gifts)  # 随机分配礼物
            lsGiftOut[person]=getGift
            gifts.remove(getGift)
            if flag==1:
                gifts.append(myGift)
    return lsGiftOut

if __name__ == '__main__':

    dictGiftOut=rd()
    print(dictGiftOut)  # 输出礼物分配情况