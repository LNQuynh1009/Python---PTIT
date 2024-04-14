n = input()
res = 0
while len(n) > 1:
    tmp = 0
    for i in n:
        tmp += ord(i) - 48
    n = str(tmp)
    res += 1

if res == 0:
    print("1")
else:
    print(res)
