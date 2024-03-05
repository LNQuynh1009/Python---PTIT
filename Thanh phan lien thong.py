from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, s, n):
        self.res = []
        visited = [False] * (n + 1)
        q = []
        q.append(s)
        visited[s] = True
        while q:
            s = q.pop(0)
            self.res.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True


n, m, k = map(int, input().split())
g = Graph()
for i in range(m):
    x, y = input().split()
    x, y = int(x), int(y)
    g.addEdge(x, y)

g.bfs(k, n)

if len(g.res) == n:
    print("0")
else:
    for i in range(1, n + 1):
        if i not in g.res:
            print(i)


"""
6 4 2
1 3
2 3
1 2
4 5
"""
