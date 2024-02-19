import operator
import re

t, k = input().split()
t, k = int(t), int(k)
a = []
for i in range(t):
    a += re.findall(r'\b\w+\b', input())
a = list(map(lambda x: x.lower(), a))
res = dict()
for i in a:
    if i in res:
        res[i] += 1
    else: res[i] = 1
ans = sorted(res.items(), key=lambda x : (-x[1], x[0]))

for key, value in ans:
    if value >= k:
        print(key, value)

"""
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi (dich benh xuat) hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""
