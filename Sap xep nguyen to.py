prime = [1] * 1001
prime[0] = prime[1] = 0
for i in range(2, 33):
    if prime[i] == 1:
        j = i * i
        while j <= 1000:
            prime[j] = 0
            j += i

n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if prime[i] == 1:
        b.append(i)

b.sort()
j = 0

for i in range(len(a)):
    if prime[a[i]] == 1:
        a[i] = b[j]
        j += 1

for i in a:
    print(i, end=" ")

"""
8
4 6 3 8 7 2 5 9
"""
