t = int(input())

while t > 0:
    n = int(input())
    a = []
    for i in range(0, n):
        a.append(int(input()))
    d = [0]*n
    cnt = -1
    res = 0
    for i in range(0, n):
        if d[i] == 0:
            if cnt < a.count(a[i]):
                cnt = a.count(a[i])
                res = a[i]
            elif cnt == a.count(a[i]):
                if a[i] < res:
                    res = a[i]
        d[i] = 1
    print(res)
    t -= 1

"""
3
3
999
999
19
4
13
333
333
13
3
11
12
13
"""