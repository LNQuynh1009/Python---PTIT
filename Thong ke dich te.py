

n, m = map(int, input().split())

a = []

for i in range(0, n):
    a.append(list(map(int, input().split())))

ax = [-1, -1, -1, 0, 0, 1, 1, 1]
ay = [-1, 0, 1, -1, 1, -1, 0, 1]
visited = [[False for _ in range(m)] for j in range(n)]

sum = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for adx, ady in zip(ax, ay):
                newi, newj = adx+i, ady+j
                if newi >= 0 and newi < n and newj >=0 and newj < m and visited[newi][newj] == False:
                    visited[newi][newj] = True
                    sum += a[newi][newj]

print(sum)


"""
4 4
1 1 0 1
2 -1 4 5
0 -1 0 0
1 0 2 1
"""