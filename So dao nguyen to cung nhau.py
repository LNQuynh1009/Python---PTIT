import math
t = int(input())

while t > 0:
    a = input()
    b = a[::-1]
    if math.gcd(int(a), int(b)) != 1:
        print("NO")
    else: print("YES")
    t -= 1

"""
1
123
997
"""