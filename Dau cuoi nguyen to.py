
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
    n1 = int(s[0:3])
    n2 = int(s[len(s)-3: len(s)])
    if d[n1] == 1 and d[n2] == 1:
        print("YES")
    else:
        print("NO")
    t -= 1

"""
3
12743
7337
12345678901234
"""