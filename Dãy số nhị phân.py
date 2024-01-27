
n = int(input())
a = list(map(int, input().split()[:n]))
cnt = 0
for i in range(0, n-1):
    if a[i]+a[i+1] == 1:
        cnt += 1
print(cnt)

"""
6
1 0 0 1 1 1
"""