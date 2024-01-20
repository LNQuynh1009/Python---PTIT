
t = int(input())

while t > 0:
    n = int(input())
    ok = 0
    for i in range(1, 1001):
        while n%7 != 0:
            n += int(str(n)[::-1])
        ok = 1
        break
    if ok == 1:
        print(n)
    else: print("-1")
    t -= 1