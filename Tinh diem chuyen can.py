
class HS:
    def __init__(self, id, name, lop):
        self.id = id
        self.name = name
        self.lop = lop
        pass
    def setcc(self, s):
        self.cc = 10 - str(s).count('v')*2 - str(s).count('m')
        self.status = ""
        if self.cc <= 0:
            self.cc = 0
            self.status = "KDDK"
    def get(self):
        return "{} {} {} {} {}".format(self.id, self.name, self.lop, self.cc, self.status)

L = []
t = int(input())
for i in range(t):
    L.append(HS(input(), input(), input()))

for i in range(t):
    msv, s = input().split()
    for j in L:
        if j.id == msv:
            j.setcc(s)

for i in L:
    print(i.get())

"""
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""