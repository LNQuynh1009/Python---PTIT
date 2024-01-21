
t = int(input())

def check(s):
    if len(s)%2 == 0:
        return False
    if s[0] == s[1]:
        return False
    res = ""
    for i in range(0, len(s), 2):
        res += s[i]
    for i in range(0, len(res)-1):
        if res[i] != res[i+1]:
            return False
    return True

while t > 0:
    s = input()
    if check(s):
        print("YES")
    else: print("NO")
    t -= 1

"""
2
2324272921262
13141516
"""