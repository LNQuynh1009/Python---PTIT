s1 = input().split()
s2 = input().split()
s1 = [i.lower() for i in s1]
s2 = [i.lower() for i in s2]

res1 = set(s1) | set(s2)
res2 = set(s1).intersection(s2)
res1 = list(res1)
res2 = list(res2)
res1.sort()
res2.sort()
for i in res1:
    print(i, end=" ")
print()
for i in res2:
    print(i, end=" ")
print()

"""
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
"""
