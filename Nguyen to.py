import math

t = int(input())
d = [1]*10005
d[0] = d[1] = 0
for i in range (2, 100):
    if d[i] == 1:
        j = i*i
        while j <= 1000:
            d[j] = 0
            j += i

while t > 0:
    n = int(input())
    k = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            k += 1
    if d[k] == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
2
2
3
"""