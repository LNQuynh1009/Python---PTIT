class SV:
    def __init__(self, id, name, lop) -> None:
        self.id, self.name, self.lop = id, name, lop

    def setCC(self, s):
        tmp = 10
        for i in s:
            if i == "v":
                tmp -= 2
            elif i == "m":
                tmp -= 1
        if tmp <= 0:
            self.cc = 0
            self.note = "KDDK"
        else:
            self.cc = tmp
            self.note = ""

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.lop} {self.cc} {self.note}"


t = int(input())
a = []
for i in range(t):
    a.append(SV(input(), input(), input()))

for i in range(t):
    msv, p = input().split()
    for sv in a:
        if sv.id == msv:
            sv.setCC(p)
            break

for i in a:
    print(i)

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
