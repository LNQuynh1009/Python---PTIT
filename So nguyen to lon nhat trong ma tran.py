d = [1] * 1026

d[0] = d[1] = 0
for i in range(2, 33):
    if d[i] == 1:
        j = i * i
        while j <= 1024:
            d[j] = 0
            j += i

n, m = input().split()
n, m = int(n), int(m)
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

res = -1

for i in a:
    for j in i:
        if d[j] == 1 and j > res:
            res = j

if res == -1:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print("Vi tri [{}][{}]".format(i, j))

"""
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
"""
