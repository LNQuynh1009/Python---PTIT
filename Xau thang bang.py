import math
t = int(input())

while t > 0:
    s1 = input()
    s2 = s1[::-1]
    ok = 1
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            ok = 0
    if ok == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
2
acxz
bcxz
"""