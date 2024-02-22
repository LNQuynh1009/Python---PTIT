def check(a, b):
    if len(a) != len(b):
        return "NO"
    for i in range(len(a)):
        if a[i] != b[i]:
            return "NO"
    return "YES"


n, m = input().split()
n, m = int(n), int(m)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = set(a)
b = set(b)
a = list(a)
b = list(b)
print(check(a, b))

"""
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
"""
