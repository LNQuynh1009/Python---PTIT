s = input()
k = int(input())
d = dict()
for i in range(0, len(s) - 1, 2):
    x = int(s[i] + s[i + 1])
    if x in d.keys():
        d[x] += 1
    else:
        d[x] = 1

tmp = {}
for key, val in d.items():
    if val >= k:
        tmp[key] = val

if tmp == {}:
    print("NOT FOUND")
else:
    for key in sorted(tmp.keys()):
        print(key, tmp[key])

"""
124356141111434356149
2
124356141111434356149
10
"""
