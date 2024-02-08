
n = int(input())
a = list(map(int, input().split()))
while len(a) < n:
    a += list(map(int, input().split()))
c = []
l = []
for i in range(n):
    if a[i]%2 == 0:
        c.append(a[i])
    else: l.append(a[i])

c.sort()
l.sort(reverse=True)
i = 0
j = 0
for k in range(n):
    if a[k]%2==0:
        print(c[i], end=' ')
        i+=1
    else:
        print(l[j], end=' ')
        j+=1

"""
10
1 2 3 4 5 6 7 7 9 6
"""