import math
t = int(input())

def check(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

d = [1]*10
d[1] = d[0] = d[4] = d[6] =d[8] = d[9] = 0
d[2] = d[3] = d[5] = d[7] = 1

def cso(n):
    for i in str(n):
        if d[int(i)] == 0:
            return False
    return True

while t > 0:
    n = int(input())
    sum = 0
    for i in str(n):
        sum += int(i)
    if check(n) and check(int(str(n)[::-1])) and cso(n) and check(sum):
        print("Yes")
    else: print("No")
    t -= 1

"""
3
13
753
757
"""