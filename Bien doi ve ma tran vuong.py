n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

b = []

for i in range(m):
    b.append([a[j][i] for j in range(n)])

if n > m:
    c = []
    for i in range(n):
        if i % 2 == 0 and i <= m - 1:
            continue
        else:
            c.append(a[i])
    a = c

if m > n:
    c = []
    for i in range(m):
        if i % 2 != 0 and i <= n - 1:
            continue
        else:
            c.append(b[i])
    res = []
    for i in range(n):
        res.append([c[j][i] for j in range(n)])
    a = res

for i in a:
    for j in i:
        print(j, end=" ")
    print()


"""
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
"""
