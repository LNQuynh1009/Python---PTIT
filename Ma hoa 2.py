
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    k = input()
    if k == '0' or k.startswith('0'):
        break
    else:
        s = k.split()
        n = int(s[0])
        tmp = s[1]
        res = ""
        for i in tmp:
            res += p[(p.index(i)+n)%28]
        print(res[::-1])

"""
1 ABCD
14 ROAD
0
"""