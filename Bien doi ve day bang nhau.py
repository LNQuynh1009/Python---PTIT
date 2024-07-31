
n = int(input())

a = list(map(int, input().split()))

res = int(1e9)
ans = -1

for i in range(0, n):
    tmp = 0
    for j in range(0, n):
        if j != i:
            tmp += abs(a[i]-a[j])
    if tmp < res:
        res = tmp
        ans = i

print(res, a[ans])

"""
8
13 5 8 7 9 15 26 34
"""