t = int(input())

while t > 0:
    n, m = input().split()
    n, m = int(n), int(m)
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    k = []
    for i in range(3):
        k.append(list(map(int, input().split())))

    res = [[0 for i in range(m - 2)] for j in range(n - 2)]
    for i in range(n - 2):
        for j in range(m - 2):
            res[i][j] = (
                k[0][0] * a[i][j]
                + k[0][1] * a[i][j + 1]
                + k[0][2] * a[i][j + 2]
                + k[1][0] * a[i + 1][j]
                + k[1][1] * a[i + 1][j + 1]
                + k[1][2] * a[i + 1][j + 2]
                + k[2][0] * a[i + 2][j]
                + k[2][1] * a[i + 2][j + 1]
                + k[2][2] * a[i + 2][j + 2]
            )
    ans = 0
    for i in res:
        for j in i:
            ans += j
    print(ans)
    t -= 1

"""
2
4 4
2 1 0 0
3 2 1 1
4 3 2 1
2 2 1 0
-1 -1 -1
-1 8 -1
-1 -1 -1
3 3
1 2 3
4 5 6
7 8 9
1 1 1
1 1 1
1 1 1
"""
