t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(0, n - 1):
        x = max(a[i], a[i + 1])
        y = min(a[i], a[i + 1])
        if x > 2 * y:
            y = 2 * y
            while y < x:
                res += 1
                y *= 2
    print(res)

"""
6
4
4 2 10 1
2
1 3
2
6 1
3
1 4 2
5
1 2 3 4 3
12
4 31 25 50 30 20 34 46 42 16 15 16
"""
