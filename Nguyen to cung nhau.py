import math
n, k = input().split()
n, k = int(n), int(k)
a = []
for i in range(10**(k-1), 10**(k)):
    if math.gcd(n, i) == 1:
        a.append(i)

for i in range(0, len(a)):
    if i != len(a) - 1 and (i+1)%10 == 0:
        print(a[i])
    else: print(a[i], end=" ")
print()