
t = int(input())

while t > 0:
    n = input()
    res = 0
    for i in n:
        res += int(i)
    if res%3 == 0:
        print("YES")
    else: print("NO")
    t -= 1

"""
2
12341
123456789123456789
"""