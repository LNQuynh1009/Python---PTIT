
d = [1]*10005
d[0] = d[1] = 0
for i in range(0, 101):
    if d[i] == 1:
        j = i*i
        while j <= 10000:
            d[j] = 0
            j += i
p = []
for i in range(2, len(d)):
    if d[i] == 1:
        p.append(i)

n, x = input().split()
n, x = int(n), int(x)
for i in range(0, n+1):
    print(x, end=' ')
    x += p[i]
print()
