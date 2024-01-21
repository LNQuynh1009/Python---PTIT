
t = int(input())

def tang(s):
    for i in range(0, len(s)-1):
        if int(s[i]) >= int(s[i+1]):
            return False
    return True

def giam(s):
    for i in range(0, len(s)-1):
        if int(s[i]) <= int(s[i+1]):
            return False
    return True

while t > 0:
    s = input()
    if len(s) < 3:
        print("NO")
        t -= 1
        continue
    ok = 0
    for i in range(0, len(s)):
        if tang(s[0:i]) and giam(s[i:]):
            ok = 1
    if ok == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
3
12342
23342
5678961
"""