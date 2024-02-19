
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(range(a[0], a[n-1]))
    res = 0
    for i in b:
        if i not in a:
           res += 1

    print(res)
    t -= 1

"""
2
5
4 5 3 8 6
3
2 1 3
"""