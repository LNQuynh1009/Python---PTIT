
t = int(input())
d = [1]*4490
d[0] = d[1] = 0
for i in range(2, 67):
    if d[i] == 1:
        j = i*i
        while j <= 4489:
            d[j] = 0
            j += i

def check(n):
    sum = 0
    for i in range(0, len(n), 2):
        sum += int(n[i])
        if int(n[i])%2 != 0:
            return False
    for i in range(1, len(n), 2):
        sum += int(n[i])
        if int(n[i])%2 == 0:
            return False
    return d[sum] == 1


while t > 0:
    n = input()
    if check(n):
        print("YES")
    else: print("NO")
    t -= 1

"""
2
2345678521
1212121212121212121212121
"""