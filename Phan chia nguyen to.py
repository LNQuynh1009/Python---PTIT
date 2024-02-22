d = [1] * 502685
d[0] = d[1] = 0
for i in range(2, 710):
    if d[i] == 1:
        j = i * i
        while j <= 502681:
            d[j] = 0
            j += i

n = int(input())
b = list(map(int, input().split()))

a = []

for i in b:
    if i not in a:
        a.append(i)

sum = 0
for i in a:
    sum += i

ans = 0
ok = 0
for i in range(0, len(a)):
    ans += a[i]
    sum -= a[i]
    if d[ans] == 1 and d[sum] == 1:
        print(i)
        ok = 1
        break

if ok == 0:
    print("NOT FOUND")

"""
10
3 6 7 3 4 7 3 6 4 4
"""
