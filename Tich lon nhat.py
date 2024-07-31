n = int(input())

a = list(map(int, input().split()))

while len(a) < n:
    a.append(list(map(int, input().split())))

a.sort(key=abs)

print(max(abs(a[n - 1] * a[n - 2]), abs(a[n - 1] * a[n - 2] * a[n - 3])))

"""
6
5 10 -2 3 -5 2
"""
