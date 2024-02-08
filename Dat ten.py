from itertools import combinations
n, k = input().split()
n, k = int(n), int(k)
tmp = input().split()
a = []
for i in tmp:
    if i not in a:
        a.append(i)
a.sort()
res = list(combinations(a, k))
for i in res:
    for j in i:
        print(j, end=' ')
    print()

"""
6 2
DONG TAY NAM BAC TAY BAC
"""