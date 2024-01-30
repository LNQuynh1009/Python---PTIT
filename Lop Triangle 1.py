import math
t = int(input())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, Point):
        d = math.sqrt((self.x-Point.x)**2 + (self.y-Point.y)**2)
        return d

def solve(d1, d2, d3):
    if d1+d2 <= d3 or d2+d3 <= d1 or d1+d3 <= d2:
        return "INVALID"
    return round(d1+d2+d3, 3)
s = []
while t > 0:
    s.append(input())
    t -= 1
for i in s:
    a = list(map(float, i.split()[:6]))
    p1 = Point(a[0], a[1])
    p2 = Point(a[2], a[3])
    p3 = Point(a[4], a[5])
    d1 = p1.dist(p2)
    d2 = p2.dist(p3)
    d3 = p3.dist(p1)
    print(solve(d1, d2, d3))
"""
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
"""