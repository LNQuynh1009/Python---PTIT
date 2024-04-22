
f1 = open("DATA1.in", 'r')

f2 = open("DATA2.in", 'r')

l1 = list(f1.read().splitlines())
l2 = list(f2.read().splitlines())
s1 = set()
s2 = set()
for i in l1:
    a = [j.lower() for j in i.split()]
    s1.update(a)

for i in l2:
    a = [j.lower() for j in i.split()]
    s2.update(a)

res1 = list(s1.difference(s2))
res2 = list(s2.difference(s1))

res1.sort()
res2.sort()

for i in res1:
    print(i, end=' ')

print()

for i in res2:
    print(i, end=' ')

