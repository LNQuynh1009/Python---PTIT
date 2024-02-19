
n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))
minn = int(1e7)
maxx = -1
for i in range(n):
    for j in range(m):
        if a[i][j] > maxx:
            maxx = a[i][j]
        if a[i][j] < minn:
            minn = a[i][j]

x = maxx - minn
ok = 0

for i in range(n):
    if x in a[i]:
        print(x)
        ok = 1
        break

for i in range(n):
    for j in range(m):
        if a[i][j] == x:
            print("Vi tri [{}][{}]".format(i, j))
if ok == 0:
    print("NOT FOUND")


"""
6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
"""