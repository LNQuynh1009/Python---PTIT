import string

TRANS = string.digits + string.ascii_uppercase

t = int(input())
while t > 0:
    k = int(input())
    n = int(input(), 2)
    s = ""
    while n > 0:
        x = n % k
        s = TRANS[x] + s
        n //= k
    print(s)
    t -= 1

"""
2
8
10010100010010101
2
10010100010010101
"""
