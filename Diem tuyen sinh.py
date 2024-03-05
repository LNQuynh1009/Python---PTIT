import re


class TS:
    def __init__(self, idx, name, diem, dtoc, kvuc):
        self.id = "TS" + "{:02d}".format(idx + 1)
        self.name = name
        self.sum = diem
        if dtoc != "Kinh":
            self.sum += 1.5
        if kvuc == "1":
            self.sum += 1.5
        if kvuc == "2":
            self.sum += 1
        if self.sum >= 20.5:
            self.status = "Do"
        else:
            self.status = "Truot"

    def getinfo(self):
        return "{} {} {:.1f} {}".format(self.id, self.name, self.sum, self.status)


def cmp(a):
    return (a.sum, (-1) * a.id)


t = int(input())
a = []
for i in range(t):
    s = input()
    ten = re.sub("\\s+", " ", s.strip()).title()
    d = float(input())
    dt = input()
    kv = input()
    a.append(TS(i, ten, d, dt, kv))

a.sort(key=cmp, reverse=True)

for i in a:
    print(i.getinfo())


"""
3
Le Thi a
22
Kinh
1
Nguyen  hong ngat
22
Kinh
1
  Chu thi MINh
14
Dao
3
"""
