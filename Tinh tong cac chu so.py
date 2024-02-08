
t = int(input())

while t > 0:
    s = input()
    res = ""
    sum = 0
    str = sorted(s)
    for i in str:
        if i.isdigit():
            sum += int(i)
        else: res += i
    print("{}{}".format(res, sum))
    t -= 1

"""
2
AC2BEW3
ACCBA10D2EW30
"""