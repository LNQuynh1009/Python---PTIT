t = int(input())
a = []
for i in range(t):
    s = input()
    j = 0
    tmp = ""
    while j < len(s):
        if s[j].isdigit():
            tmp += s[j]
        else:
            if len(tmp) > 0:
                a.append(int(tmp))
            tmp = ""
        j += 1
    if len(tmp) > 0:
        a.append(int(tmp))

a.sort()
for i in a:
    print(i)

"""
3
A129h
G07bxjq3
aaaaaaa4aaaa
"""
