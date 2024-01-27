
n, m = input().split()
n, m = int(n), int(m)

d = [1]*1005
d[0] = d[1] = 0
for i in range(2, 101):
    if d[i] == 1:
        j = i*i
        while j <= 1000:
            d[j] = 0
            j += i
a = []
for i in range(0, n):
    tmp = []
    tmp = list(map(int, input().split()[:m]))
    a.append(tmp)
for i in range(0, n):
    for j in range(0, m):
        a[i][j] = d[a[i][j]]
for i in range(0, n):
    for j in range(0, m):
        print(a[i][j], end=' ')
    print()

"""
3 3
1 2 3
4 5 6
7 8 9
"""