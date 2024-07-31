from string import ascii_uppercase

D = dict(zip(ascii_uppercase, range(len(ascii_uppercase))))


def devide(s):
    n = len(s) // 2
    return s[:n], s[n:]


def rotate(d):
    r = sum(map(lambda i: D[i], d))
    return "".join(map(lambda i: ascii_uppercase[(D[i] + r) % len(D)], d))


def merge(r1, r2):
    return "".join(
        map(lambda i1, i2: ascii_uppercase[(D[i1] + D[i2]) % len(D)], r1, r2)
    )


for _ in range(int(input())):
    s = input()
    d1, d2 = devide(s)
    r1, r2 = rotate(d1), rotate(d2)
    m = merge(r1, r2)
    print(m)

"""
3
EWPGAJRB
BB
TPQJDRJWSQXGRRIPXFMINTELHBJA
"""
