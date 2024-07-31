from sys import stdin
from math import sqrt
from array import array

n = 2 * 10**6
res = array("i", [0] * (n + 1))

for i in range(2, int(sqrt(n)) + 1):
    if res[i] == 0:
        res[i] = i
        for j in range(n // i + 1):
            res[i * j] = i

for i in range(4, n + 1):
    res[i] += res[i // res[i]] if res[i] else i

sum = 0
t, it = int(stdin.readline()), 0

while it < t:
    sum += res[(int(stdin.readline()))]
    it += 1

print(sum)

"""
5 
7
9 
10 
13 
100
"""
