
t = int(input())

while t > 0:
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    res = str(sum)
    if len(res) > 1 and res == res[::-1]:
        print("YES")
    else: print("NO")
    t -= 1

"""
2
12341
22222222222222222222
"""