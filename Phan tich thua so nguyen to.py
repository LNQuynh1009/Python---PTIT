import math
t = int(input())

while t > 0:
    n = int(input())
    d = []
    while n%2 == 0:
        d.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            d.append(i)
            n /= i
    if n>2:
        d.append(n)
    d.sort()
    res = ""
    res += "1 * "
    res += "{}^{} * ".format(int(d[0]), d.count(d[0]))
    for i in range(1, len(d)):
        if d[i] != d[i-1]:
            res += "{}^{} * ".format(int(d[i]), d.count(d[i]))
    print(res[:len(res)-2])
    t -= 1

"""
3
28
100
1234
"""