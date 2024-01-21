
t = int(input())
d = [1]*4625
d[0] = d[1] = 0
for i in range(2, 69):
    if d[i] == 1:
        j = i*i
        while j <= 4624:
            d[j] = 0
            j += i

while t > 0:
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if d[sum] == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
2
12341
22222222222222222222
"""