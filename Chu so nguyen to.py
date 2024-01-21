
t = int(input())

d = [1]*530
d[1] = d[0] = 0
for i in range(2, 24):
    if d[i] == 1:
        j = i*i
        while j <= 529:
            d[j] = 0
            j += i

def check(n):
    if d[len(n)] == 0:
        return "NO"
    cnt = 0
    for i in n:
        if d[int(i)] == 0:
            cnt += 1
    if (len(n)-cnt) < cnt:
        return "NO"
    return "YES"

while t > 0:
    n = input()
    print(check(n))
    t -= 1

"""
3
1234567
22334455667
23400300489898989
"""