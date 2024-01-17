
t = int(input())

while t > 0:
    s = input()
    res = ""
    for i in range(0, len(s)):
        if s[i].isdigit():
            n = int(s[i])
            res += s[i-1]*n
    print(res)
    t -= 1

"""
2
A8
A2E1C4G3D1
"""