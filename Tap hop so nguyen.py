
n, m = input().split()
n, m = int(n), int(m)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = set(a)
B = set(b)
i = sorted(list(A&B))
D1 = sorted(list(A-B))
D2 = sorted(list(B-A))
print(*i)
print(*D1)
print(*D2)

"""
5 6
1 2 3 4 5
3 4 5 6 7 8
"""