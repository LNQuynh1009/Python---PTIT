
t = int(input())

def check(n):
    for i in range(0, len(n) - 2):
        if n[i] != n[i+2]:
            return False
    dic = []
    for i in n:
        if i not in dic:
            dic.append(i)
    return len(dic) == 2

while t > 0:
    n = input()
    if check(n):
        print("YES")
    else: print("NO")
    t -= 1

"""
3
12121212
343433
78789989
"""