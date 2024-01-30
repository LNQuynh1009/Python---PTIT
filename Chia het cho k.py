
a, k, n = input().split()
a, k, n = int(a), int(k), int(n)
res = []
l = n//k
for i in range(1, l+1):
    if k*i <= n and k*i-a>0:
        res.append(k*i-a)
if res == []:
    print("-1")
else:
    for i in res:
        print(i, end=' ')
