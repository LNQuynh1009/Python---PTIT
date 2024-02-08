
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    for i in b:
        if a.count(i)%2 != 0:
            print(i)
            break
    t -= 1

"""
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
"""