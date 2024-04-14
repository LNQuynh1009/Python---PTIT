n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

res = [0] * n

if n > 2:
    for i in range(0, n):
        res[i] = (
            a[i][int((i + 1) % n)]
            + a[i][int((i + 2) % n)]
            - a[int((i + 1) % n)][int((i + 2) % n)]
        )
        res[i] /= 2
else:
    res[0] = a[0][1] / 2
    res[1] = a[1][0] / 2

res = [int(i) for i in res]

for i in res:
    print(i, end=" ")

print()

"""
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
2
0 2
2 0
"""
