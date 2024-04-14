
import math

l, r = (int(x) for x in input().split())
a = [None]*3
def backtrack(n, start):
    if n == 3:
        if math.gcd(a[0], a[1]) == math.gcd(a[1], a[2]) == math.gcd(a[0], a[2]) == 1:
            print(f"({a[0]}, {a[1]}, {a[2]})")
        return
    for i in range(start, r+1, 1):
        a[n] = i
        backtrack(n+1, i)

backtrack(0, l)