
t = int(input())

while t > 0:
    s = input()
    ok = 1
    for i in range(0, len(s)-1):
        if int(s[i]) > int(s[i+1]):
            ok = 0
            break
    if ok == 1:
        print("YES")
    else: print("NO")
    t -= 1

"""
2
12345678888888888888889
65645645465754765876857685846
"""