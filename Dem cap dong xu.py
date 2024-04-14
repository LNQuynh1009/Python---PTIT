from math import comb

n = int(input())
a = []
for i in range(n):
    tmp = " ".join(input())
    a.append(tmp.split())
c = [0]*n
h = [0]*n

for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            c[j] += 1
            h[i] += 1

res = 0
for i in c:
    res += comb(i, 2)
for i in h:
    res += comb(i, 2)
print(res)
"""
4
CC..
C..C
.CC.
.CC.
"""