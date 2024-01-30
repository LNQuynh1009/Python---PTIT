
t = int(input())

while t > 0:
    s = input().split()
    a = list(map(float, s[:len(s)]))
    n = a[0]
    l = a[1]
    m = a[2]
    cnt = 0
    while n < m:
        n = n*(1+l/100)
        cnt += 1
    print(cnt)
    t -= 1

"""
2
200.00 6.5 300
500 4 1000.00
"""