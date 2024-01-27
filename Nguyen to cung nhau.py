import math
n = int(input())
a = list(map(int, input().split()[:n]))
a.sort()
for i in range(0, n-1):
    for j in range(i+1, n):
        if math.gcd(a[i], a[j]) == 1:
            print(a[i], end=' ')
            print(a[j])

"""
5
3 7 9 6 13
"""