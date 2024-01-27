
t = int(input())

def cmp(s1, s2):
    c1 = 0
    c2 = 0
    for i in s1:
        c1 += int(i)
    for i in s2:
        c2 += int(i)
    if c1 == c2:
        return int(s1) > int(s2)
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