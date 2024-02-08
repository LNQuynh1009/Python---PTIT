
d = [1]*1025
d[0] = d[1] = 0
for i in range(2, 33):
    if d[i] == 1:
        j = i*i
        while j <= 1024:
            d[j] = 0
            j += i
n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if d[i] == 1:
        b.append(i)
b.sort()
i = j = 0
while i < n:
    if d[a[i]] == 1:
        a[i] = b[j]
        j += 1
    i +=1

print(*a)
"""
8
4 6 3 8 7 2 5 9
"""