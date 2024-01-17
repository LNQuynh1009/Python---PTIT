import math

t = int(input())
d = []
d = [1]*10005
d[0] = d[1] = 0

for i in range(2, 100):
    if d[i] == 1:
        j = i*i
        while j <= 10000:
            d[j] = 0
            j += i

while t > 0:
    [a, b] = input().split()
    a, b = int(a), int(b)
    n = str(math.gcd(a, b))
    cnt = 0
    for i in n:
        cnt += int(i)
    if d[cnt] == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
3
28 42
123 18
550 55
"""