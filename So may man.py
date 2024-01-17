
s = input()
bon = 0
bay = 0
for i in s:
    if i == '4':
        bon += 1
    elif i == '7':
        bay += 1

if (bon+bay) == 4 or (bon+bay) == 7:
    print("YES")
else: print("NO")