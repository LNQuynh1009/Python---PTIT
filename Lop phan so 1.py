import math
a, b = input().split()
a, b = int(a), int(b)

d = math.gcd(a, b)
a = a//d
b = b//d
print('{}/{}'.format(a, b))