
class Tram:
    def __init__(self, idx, name):
        self.name = name
        self.id = "T" + "{:02d}".format(idx)
        self.time = 0
        self.q = 0
        pass
    def setlm(self, st, en, q):
        start = list(map(int, st.split(':')))
        end = list(map(int, en.split(':')))
        self.time += (end[0]*60 + end[1] - start[0]*60 - start[1])/60
        self.q += q
    def get(self):
        self.tb = self.q/self.time
        return "{} {} {:.2f}".format(self.id,self.name,self.tb)

t = int(input())
a = []
idx = 1
for i in range(t):
    s = input()
    ok = None
    for j in a:
        if j.name == s:
            ok = j
            break
    if ok != None:
        ok.setlm(input(), input(), int(input()))
    else:
        x = Tram(idx, s)
        x.setlm(input(), input(), int(input()))
        a.append(x)
        idx += 1

for i in a:
    print(i.get())

"""
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
"""