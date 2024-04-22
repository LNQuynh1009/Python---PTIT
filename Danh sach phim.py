
import datetime

class TL:
    def __init__(self,stt, tl):
        self.ma = "TL{:03d}".format(stt)
        stt += 1
        self.tl = tl

    def show(self):
        print(self.ma, self.tl)

class Phim:
    def __init__(self, stt, ngay, ten, tap, tl):
        self.ma = "P{:03d}".format(stt)
        self.ngay = ngay
        self.day = int(ngay[0:2])
        self.month = int(ngay[3:5])
        self.year = int(ngay[6:])
        self.ten = ten
        self.tap = tap
        self.tl = tl

    def show(self):
        print("{} {} {} {} {}".format(self.ma, self.tl, self.ngay, self.ten, self.tap))

n, m = map(int, input().split())

TL_List = []

for i in range(1, n+1):
    tl = input()
    TL_List.append(TL(i,tl))

PhimList = []

for i in range(1, m+1):
    ma = input()
    tl = ""
    for j in TL_List:
        if j.ma == ma:
            tl = j.tl
            break

    PhimList.append(Phim(i, input(), input(), input(), tl))

PhimList.sort(key=lambda x: (x.year, x.month, x.day))

for i in PhimList:
    i.show()

"""
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
"""