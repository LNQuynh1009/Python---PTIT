
t = int(input())

while t > 0:
    n, m, k = input().split()
    n, m, k = int(n), int(m), int(k)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    res = []
    i = j = l = 0
    while i < n and j < m and l < k:
        if a[i] == b[j] and b[j] == c[l]:
            res.append(a[i])
            i+=1
            j+=1
            l+=1
        elif a[i] <= b[j] and a[i] <= c[l]:
            i+=1
        elif b[j] <= a[i] and b[j] <= c[l]:
            j += 1
        elif c[l] <= a[i] and c[l] <= b[j]:
            l += 1
    if res == []:
        print("NO")
    else:
        for i in res:
            print(i, end=' ')
        print()
    t -= 1

"""
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
"""