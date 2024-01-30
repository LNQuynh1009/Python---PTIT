import math
class HD:
    def __init__(self,idx, name, n):
        self.name = name
        res = 0
        if n > 50:
           res = 50*100
           if n > 100:
               res += 50 * 150
               res += (n - 100) * 200
               res = round(res * 1.05)
           else:
               res += (n - 50) * 150
               res = round(res * 1.03)
        else:
            res = n*102
        self.sum = res
        self.id = "KH" + "{:02d}".format(idx)
    def get(self):
        return "{} {} {}".format(self.id, self.name, self.sum)

def cmp(a):
    return a.sum

t = int(input())
L = []
for i in range(t):
    L.append(HD(i+1, input(), -int(input()) + int(input())))

L.sort(key=cmp, reverse=True)

for i in L:
    print(i.get())

"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""