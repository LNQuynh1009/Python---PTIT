
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    a.sort()
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            if a[i]+a[l]+a[r] == 0:
                cnt += 1
                l += 1
            elif a[i]+a[l]+a[r] > 0:
                r-=1
            else: l+=1
    print(cnt)
    t-=1

"""
2
5
0 -1 2 -3 1 
5
1 -2  1  0  5
"""