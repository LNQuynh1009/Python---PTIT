visited = [False] * 100
graph = [[] for _ in range(1, 101)]


def bfs(s, z):
    q = []
    q.append(s)
    while q:
        x = q.pop(0)
        for v in graph[x]:
            if visited[v] == False and v != z:
                q.append(v)
                visited[v] = True


t = int(input())

while t > 0:
    n, m = map(int, input().split())
    visited = [False] * 101
    graph = [[] for _ in range(1, 101)]
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    lt = 1
    res = 0

    for i in range(1, n+1):
        visited = [False] * 101
        l = 0
        for j in range(1, n+1):
            if j != i and visited[j] == False:
                l += 1
                bfs(j, i)
        if l > lt:
            lt = l
            res = i

    if lt == 1:
        print("0")

    else:
        print(res)
    t -= 1

"""
2
5 5
1 2
1 3
2 3
3 4
3 5
5 7
1 2
1 3
2 3
2 5
3 4
3 5
4 5
"""