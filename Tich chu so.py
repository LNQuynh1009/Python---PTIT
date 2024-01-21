
t = int(input())

while t > 0:
    n = input()
    res = 1
    for i in n:
        if i != "0":
            res *= int(i)
    print(res)
    t -= 1

"""
2
123410
123456789123456789
"""