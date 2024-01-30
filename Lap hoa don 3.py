
class HD:
    def __init__(self, id, name, sl, dg, ck):
        self.id = id
        self.name = name
        self.sl = sl
        self.dg = dg
        self.ck = ck
        self.sum = self.sl*self.dg - self.ck
    def get(self):
        return "{} {} {} {} {} {}".format(self.id, self.name, self.sl, self.dg, self.ck, self.sum)

def cmp(a):
    return a.sum

t = int(input())

L = []
for i in range(t):
    L.append(HD(input(), input(), int(input()), int(input()), int(input())))

L.sort(key=cmp, reverse=True)

for i in L:
    print(i.get())

"""
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
"""