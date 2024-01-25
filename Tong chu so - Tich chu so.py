
t = int(input())

def check(s):
    for i in range(1, len(s), 2):
        if s[i] != '0':
            return False
    return True

while t > 0:
    s = input()
    sum = 0
    mul = 1
    for i in range(0, len(s), 2):
        sum += int(s[i])
    if check(s):
        mul = 0
    else:
        for i in range(1, len(s), 2):
            if s[i] != '0':
                mul *= int(s[i])
    print(sum, mul)
    t -= 1

"""
3
12345678
20000
22334455667788
"""
