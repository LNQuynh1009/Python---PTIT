f = open("CONTACT.in", "r")
a = set()
for x in f:
    a.add(x.lower().rstrip("\n"))

b = list(a)
b.sort()
for i in b:
    print(i)
