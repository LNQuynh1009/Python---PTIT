
t = int(input())

def check(s):
    for i in s:
        if i != '1' and i != '0' and i != '2':
            return "NO"
    return "YES"

while t > 0:
    s = input()
    print(check(s))
    t -= 1

"""
3
1214AB
10210221
22222222
"""