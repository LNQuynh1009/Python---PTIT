
t = int(input())

def cmp(a1, a2):
    c1 = 1
    c2 = 1
    for i in a1:
        c1 *= int(i)
        if c1 == 0:
            break
    for i in a2:
        c2 *= int(i)
        if c2 == 0:
            break
    if c1 == c2:
        return int(a1) > int(a2)
    return c1 > c2

while t > 0:
    n = int(input())
    a = input().split()
    for i in range(0, n-1):
        for j in range(i, n):
            if cmp(a[i], a[j]):
                a[i], a[j] = a[j], a[i]
    for i in a:
        print(i, end=' ')
    print()
    t -= 1

"""
1
8
143 43 22 99 7 9 1111 10000000
"""