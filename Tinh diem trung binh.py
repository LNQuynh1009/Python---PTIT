
class Student:
    def __init__(self, idx, name, d1, d2, d3):
        self.id = "SV" + "{:02d}".format(idx)
        str = name.split()
        res = ""
        for i in str:
            res += i.title()+" "
        self.name = res
        self.tb = (d1*3+d2*3+d3*2)/8
        self.tb = round(self.tb+ 0.0000000001,2)
        self.rank = 0
    def get(self):
        return "{} {}{:.2f} {}".format(self.id, self.name, self.tb, self.rank)

def cmp(a):
    return -a.tb

t = int(input())
a = []
for i in range(t):
    a.append(Student(i+1, input().strip(), float(input()), float(input()), float(input())))
a.sort(key=cmp)
for i in range(len(a)):
    if a[i].tb == a[i-1].tb and i > 0:
        a[i].rank = a[i-1].rank
    else:
        a[i].rank = i+1

for i in a:
    print(i.get())

"""
2
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
"""