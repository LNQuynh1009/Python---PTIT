import math
t = int(input())

while t > 0:
    n = input()
    a = [int(i) for i in n]
    for i in range(len(a)-1, 0, -1):
        if a[i] > 4:
            a[i-1] = a[i-1]+1
        a[i] = 0
    print(''.join([str(i) for i in a]))
    t -= 1

"""
7
15
14
5
99
12345678
44444445
1445
"""