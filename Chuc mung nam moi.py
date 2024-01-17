
t = int(input())
dic = set()
while t > 0:
    s = input()
    if s not in dic or dic == {}:
        dic.add(s)
    t -= 1
print(len(dic))

"""
4
CHUC MUNG NAM MOI
HAPPY NEW YEAR
CHUC MUNG TUOI MOI
CHUC MUNG NAM MOI
"""