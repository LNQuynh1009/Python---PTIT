
n = int(input())

d = [1]*1000005
d[0] = d[1] = 0
for i in range(0, 1001):
    if d[i] == 1:
        j = i*i
        while j <= int(1e6):
            d[j] = 0
            j += i

a = list(map(int, input().split()[:n]))
k = [0]*1000005
for i in range(0, n):
    if k[a[i]] == 0 and d[a[i]] == 1:
        print(a[i], a.count(a[i]))
        k[a[i]] = 1

"""
10
2 4 7 5 7 8 9 3 7 2
"""