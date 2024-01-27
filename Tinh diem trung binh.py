
n = int(input())
a = list(map(float, input().split()[:n]))
a.sort()
maxx = a[n-1]
minn = a[0]
sum = 0
cnt = 0
for i in range(1, n-1):
    if a[i] == maxx or a[i] == minn:
        continue
    else:
        sum += a[i]
        cnt += 1
print(round(sum/cnt, 2))

"""
6
6.75 8 9.2 7.25 7.75 6.75
"""
