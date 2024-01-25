
t = int(input())
d = [1]*530
d[0] = d[1] = 0
for i in range(2, 24):
    if d[i] == 1:
        j = i*i
        while j <= 529:
            d[j] = 0
            j += i

def check(s):
    for i in range(0, len(s)):
        if d[int(s[i])] != d[i]:
            return "NO"
    return "YES"

while t > 0:
    s = input()
    print(check(s))
    t -= 1

"""
2
14239567
2314514535353
"""