s = input().split()
while len(s) != 10:
    s += input().split()

a = list(map(int, s[:10]))
s = set()
for i in range(0, 10):
    s.add(a[i] % 42)
print(len(s))
"""
1 2 3 4 5 6  7 8  9 10
42 84 252 420 840
126 42 84 420 126
39 40 41 42 43 44 82
83 84 85
"""