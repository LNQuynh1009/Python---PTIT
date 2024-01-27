
t = int(input())

while t > 0:
    s = input()
    res = ""
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res += str(cnt) + s[i-1]
            cnt = 1
        else: cnt+=1
    if s[len(s)-1] == s[len(s)-2]:
        res += str(cnt) + s[len(s)-1]
    else: res += "1" + s[len(s)-1]
    print(res)
    t -= 1
"""
3
AACDDPQ
11111147g
1111111111
"""