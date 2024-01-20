
t = int(input())

def check(n):
    sum = 0
    for i in range(0, len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) != 2:
            return False
        sum += int(n[i])
    sum += int(n[len(n)-1])
    return sum%10 == 0

while t > 0:
    n = input()
    if check(n):
        print("YES")
    else: print("NO")
    t -= 1

"""
3
1353
246864
123435
"""