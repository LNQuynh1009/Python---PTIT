
t = int(input())

d = [1]*1000005
d[0] = d[1] = 0
for i in range(2, 1001):
    if d[i] == 1:
        j = i*i
        while j <= int(1e6):
            d[j] = 0
            j += i

while t >0:
    cnt = 0
    n = int(input())
    for i in range(n):
        if d[i] == 1:
            if (d[i+2] == 1 and d[i+6] == 1 and i+2 < n and i+6 < n) or (d[i+4] == 1 and d[i+6] == 1 and i+4 < n and i+6 < n):
                cnt += 1
    print(cnt)
    t -= 1

"""
2
15
25
"""