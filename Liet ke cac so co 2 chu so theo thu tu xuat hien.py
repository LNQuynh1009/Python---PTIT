
s = input()
a = []
for i in range(0, len(s)-1, 2):
    tmp = int(s[i] + s[i+1])
    if tmp not in a:
        a.append(tmp)

for i in a:
    print(i, end=' ')