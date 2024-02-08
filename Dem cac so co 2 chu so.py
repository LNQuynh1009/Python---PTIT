
class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get(self):
        print(self.x, self.y)

s = input()
a = []
for i in range(0, len(s)-1, 2):
    tmp = int(s[i] + s[i+1])
    ok = 0
    for j in a:
        if j.x == tmp:
            j.y +=1
            ok = 1
    if ok == 0:
        a.append(pair(tmp, 1))

for i in a:
    i.get()