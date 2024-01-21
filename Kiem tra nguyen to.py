
t = int(input())
d = [1]*10005

d[0] = d[1] = 0

for i in range(2, 101):
    if d[i] == 1:
        j = i*i
        while j <= 10000:
            d[j] = 0
            j += i

while t > 0:
    s = input()
    n = int(s[len(s)-4:])
    if d[n] == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
3
12234323130097
3443354654654654461123
43543543434554659999
"""