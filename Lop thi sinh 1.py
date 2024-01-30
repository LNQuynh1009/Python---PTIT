
class TS:
    def __init__(self, name, bd, sum):
        self.name = name
        self.bd = bd
        self.sum = sum
    def out(self):
        print(self.name, self.bd, f"{self.sum:.1f}")

if __name__ == '__main__':
    ten = input()
    ns = input()
    if ns[2] != '/':
        ns = "0" + ns
    if ns[5] != '/':
        ns = ns[:3] + '0' + ns[3:]
    p1 = float(input())
    p2 = float(input())
    p3 = float(input())
    ts = TS(ten, ns, p1+p2+p3)
    ts.out()

"""
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
"""