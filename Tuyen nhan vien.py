
class NV:
    def __init__(self, idx, name, lt, th):
        self.name = name
        self.id = "TS0" + str(idx)
        if lt > 10:
            lt /= 10
        if th > 10:
            th /= 10
        self.tb = (lt+th)/2
        if self.tb < 5:
            self.status = "TRUOT"
        elif self.tb < 8:
            self.status = "CAN NHAC"
        elif self.tb < 9.5:
            self.status = "DAT"
        else: self.status = "XUAT SAC"
    def get(self):
        return "{} {} {:.2f} {}".format(self.id, self.name, self.tb, self.status)

def cmp(a):
    return a.tb

L = []

t = int(input())

for i in range(t):
    L.append(NV(i+1, input(), float(input()), float(input())))

L.sort(key=cmp, reverse=True)

for i in L:
    print(i.get())

"""
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
"""