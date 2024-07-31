import string

TRANS = string.digits + string.ascii_uppercase

t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    s = ""
    while n > 0:
        tmp = n % b
        s = TRANS[tmp] + s
        n = int(n / b)
    print(s)

"""
3
10 2
2021 2
31 16
"""
