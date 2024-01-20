
t = int(input())
d = [1]*1000005

d[0] = d[1] = 0
for i in range(2, 1001):
    if d[i] == 1:
        j = i*i
        while j <= int(1e6):
            d[j] = 0
            j += i

while t > 0:
    n = input()
    dic = []
    for i in range(13, int(n)):
        if d[i] == 1:
            j = int(str(i)[::-1])
            if j == i or j in dic or j >= int(n) or d[j] == 0:
                continue
            else:
                dic.append(i)
                dic.append(j)
    for i in dic:
        print(i, end=' ')
    print()
    t -= 1