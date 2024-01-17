
t = int(input())

while t > 0:
    s = input()
    if s[0]+s[1] == s[len(s)-2]+s[len(s)-1]:
        print("YES")
    else: print("NO")
    t -= 1

"""
3
12321
1234512
10233211111
"""