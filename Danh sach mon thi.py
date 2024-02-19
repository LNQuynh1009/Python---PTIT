
class MH:
    def __init__(self, id, name, ht):
        self.id = id
        self.name = name
        self.ht = ht
    def get(self):
        return "{} {} {}".format(self.id, self.name, self.ht)

def cmp(a):
    return a.id

L = []

for i in range(int(input())):
    L.append(MH(input(), input(), input()))

L.sort(key=cmp)

for i in L:
    print(i.get())

"""
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
"""