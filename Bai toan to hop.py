from itertools import combinations
n, k = input().split()
n, k = int(n), int(k)
a = list(map(int, input().split()[:n]))
a = list(dict.fromkeys(a))
a.sort()
res = list(combinations(a, k))
ans = []
for i in res:
    for j in i:
        print(j, end=' ')
    print()
"""
8 3
2 4 4 3 5 1 3 4
"""