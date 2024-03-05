def palin(x):
    s = str(x)
    return s == s[::-1] and len(s) > 1


n, m = input().split()
n, m = int(n), int(m)

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

res = -1
for i in a:
    for j in i:
        if palin(j) and j > res:
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
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
"""
