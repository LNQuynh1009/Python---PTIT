
t = int(input())
d = [1]*93
d[0] = 0
d[1] = d[2] = 1
for i in range(3, 93):
    d[i] = d[i-1] + d[i-2]

while t > 0:
    a, b = input().split()
    a, b = int(a), int(b)
    for i in range(a, b+1):
        print(d[i], end=' ')
    print()
    t -= 1

"""
1
1 10
"""