
while True:
    s = list(map(int, input().split()))
    if s == [0, 0, 0, 0]:
        break
    cnt = 0
    while len(set(s)) > 1:
        b = []
        for i in range(3):
            b.append(abs(s[i]-s[i+1]))
        b.append(abs(s[3]-s[0]))
        s = b
        cnt += 1
    print(cnt)

"""
1 3 5 9
4 3 2 1
0 0 0 0
"""