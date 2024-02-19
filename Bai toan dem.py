
n = int(input())
a = list(map(int, input().split()))
while len(a) < n:
    a += list(map(int, input().split()))

res = set(range(1, a[-1]+1)) - set(a)

if len(res) > 0:
    for i in res:
        print(i)
else:
    print("Excellent!")
"""
4
1 2 3 5
7
4 5 7 8 9
10 11
5
1 2 3
4
5
"""