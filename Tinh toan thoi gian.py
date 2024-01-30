
class KH:
    def __init__(self, id, name, st, en):
        self.id = id
        self.name = name
        self.sum = int(en[:2])*60 + int(en[3:]) - (int(st[:2])*60 + int(st[3:]))
        self.g = self.sum//60
        self.p = self.sum-self.g*60
    def get(self):
        return "{} {} {} gio {} phut".format(self.id, self.name, self.g, self.p)

def cmp(a):
    return a.sum

L = []

t = int(input())

for i in range(t):
    L.append(KH(input(), input(), input(), input()))

L.sort(key = cmp, reverse=True)

for i in L:
    print(i.get())

"""
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
"""