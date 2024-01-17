
s = input()
hoa = 0
thuong = 0
for i in s:
    if i.isupper():
        hoa += 1
    else: thuong += 1
if thuong >= hoa:
    print(s.lower())
else: print(s.upper())