t = int(input())
while t > 0:
    [n, d] = (input().split())
    n, d = int(n), int(d)
    a = list(map(int, input().split()))
    b = []
    for i in range(d, n):
        print(a[i], end=' ')
    for i in range(0, d):
        print(a[i], end=' ')
    print()
    t -= 1

"""
2
5 2
1 2 3 4 5 
10 3
2 4 6 8 10 12 14 16 18 20
"""