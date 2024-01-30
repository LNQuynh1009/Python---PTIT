
class GV:
    def __init__(self, idx, name, xt, th, cm):
        self.id = "GV" + "{:02d}".format(idx)
        self.name = name
        if xt[0] == 'A':
            self.chuyen = "TOAN"
        elif xt[0] == 'B':
            self.chuyen = "LY"
        else: self.chuyen = "HOA"
        ut = 0
        if xt[1] == '1':
            ut = 2.0
        elif xt[1] == '2':
            ut = 1.5
        elif xt[1] == '3':
            ut = 1.0
        else: ut = 0.0
        self.sum = cm + th*2 + ut
        if self.sum >= 18.0:
            self.status = "TRUNG TUYEN"
        else: self.status = "LOAI"
    def get(self):
        return "{} {} {} {:.1f} {}".format(self.id, self.name, self.chuyen, self.sum, self.status)\

def cmp(a):
    return a.sum

t = int(input())
L = []
for i in range(t):
    L.append(GV(i+1, input(), input(), float(input()), float(input())))

L.sort(key=cmp, reverse=True)

for i in L:
    print(i.get())

"""
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
"""