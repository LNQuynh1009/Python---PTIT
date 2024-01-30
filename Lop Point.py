import math
from decimal import *
class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def distance(self, Point):
        dist = math.sqrt((self.p1-Point.p1)**2 + (self.p2-Point.p2)**2)
        return f"{dist:.4f}"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1