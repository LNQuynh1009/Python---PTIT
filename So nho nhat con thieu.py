
n = int(input())
res = [i for i in range(1, n+2)]
a = list(map(int, input().split()[:n]))
for i in a:
    if i in res:
        res.remove(i)
print(res[0])