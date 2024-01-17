
t = int(input())

while (t > 0):
    s = input()
    ok = 1
    for i in s:
        if i != "4" and i != "7":
            ok = 0
            break
    if(ok == 1):
        print("YES")
    else: print("NO")
    t -= 1

"""
3
4477
44444487777777777
47474747474777777777777744444
"""