from collections import Counter
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()[:n]))
    count = Counter(a)
    res = count.most_common(1)[0][1]
    ans = count.most_common(1)[0][0]
    if res <= int(n/2):
        print("NO")
    else: print(ans)
    t -= 1

"""
2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4
"""