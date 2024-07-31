from math import inf
prime = [1]*10005

prime[0] = prime[1] = 0
for i in range(2, 101):
    if prime[i] == 1:
        j = i*i
        while j <= 10000:
            prime[j] = 0
            j += i

def up(n):
    res = 0
    while prime[n+res] == 0:
        res += 1
    return res

def down(n):
    res = 0
    while prime[n-res] == 0 and (n-res) >=2:
        res += 1
    return res if (n-res) >= 2 else inf

n = int(input())

a = list(map(int, input().split()))

res = 0
for i in a:
    res = max(res, min(up(i), down(i)))

print(res)
"""
8
13 5 8 7 9 15 26 34
"""
