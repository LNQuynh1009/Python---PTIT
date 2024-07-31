import string

TRANS = string.digits + string.ascii_uppercase

f = open("DATA.in", "r")
t = int(f.readline())

while t > 0:
    k = int(f.readline())
    n = f.readline().strip("\n")
    n = int(n, 2)
    res = ""
    while n > 0:
        res = TRANS[n % k] + res
        n //= k
    print(res)
    t -= 1
