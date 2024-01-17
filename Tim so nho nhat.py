import sys

t = int(input())
while t > 0 :
    s = input()
    s += 'a'
    res = sys.maxsize
    l = len(s)
    x = 0
    for i in range(0, l-1):
        if(s[i].isdigit()):
            x = x*10 + int(s[i])
            if(s[i+1].isalpha()):
                res = min(res, x)
                x = 0
    print(res)
    t -= 1
"""
2
12ab29cd19
ab123gh456cd
"""