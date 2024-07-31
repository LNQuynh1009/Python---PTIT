def check(adj, n):
    if n == 1:
        return "Yes"
    deg = [0] * (n + 1)
    for i in range(n + 1):
        for v in adj[i]:
            deg[v] += 1

    countCen = 0
    cen = 0
    for i in range(1, n + 1):
        if deg[i] == n - 1:
            countCen += 1
            cen = i
    if countCen != 1:
        return "No"
    for i in range(1, n + 1):
        if i == cen:
            continue
        if deg[i] != 1:
            return "No"
    return "Yes"


n = int(input())
adj = [[] for i in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(check(adj, n))

"""
5
1 2
1 3
1 4
1 5
"""
