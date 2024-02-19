
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

k = int(input())

up = down = 0

for i in range(n):
    for j in range(0, n-i-1):
        up += a[i][j]

for i in range(n):
    for j in range(n-i, n):
        down += a[i][j]

res = abs(up-down)
if res <= k:
    print("YES")
else: print("NO")

print(res)
"""
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
"""