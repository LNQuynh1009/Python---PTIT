t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()[:n]))
    b = list(map(int, input().split()[:n]))
    a.sort()
    b.sort()
    ok = 1
    for i in range(0, n):
        if a[i] > b[i]:
            ok = 0
            break
    if ok == 0:
        print("NO")
    else: print("YES")
    t -= 1
"""
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84
"""