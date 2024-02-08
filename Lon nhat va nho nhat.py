
while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    if a[0] == a[-1]:
        print("BANG NHAU")
    else: print("{} {}".format(a[0], a[-1]))

"""
5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0
"""