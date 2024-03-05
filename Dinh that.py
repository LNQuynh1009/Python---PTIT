from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s, n, z, v):
        self.res = []
        visited = [False] * (n + 1)
        q = []
        q.append(s)
        visited[s] = True
        while q:
            s = q.pop(0)
            self.res.append(s)
            for i in self.graph[s]:
                if visited[i] == False and i != z:
                    q.append(i)
                    visited[i] = True
        return visited[v] == 0


t = int(input())

while t > 0:
    n, m, u, v = map(int, input().split())
    g = Graph()
    cnt = 0
    for i in range(m):
        x, y = input().split()
        x, y = int(x), int(y)
        g.addEdge(x, y)
    for i in range(1, n + 1):
        if i != u and i != v:
            if g.bfs(u, n, i, v):
                cnt += 1
    print(cnt)
    t -= 1


"""
2
5 7 1 3
1 2
2 4
2 5
3 1
3 2
4 3
5 4
4 5 1 4
1 2
1 3
2 3
2 4
3 4
"""
