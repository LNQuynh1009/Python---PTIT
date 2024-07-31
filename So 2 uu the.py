res = []


def find_all():
    q = ["1", "2"]
    dem = 0
    while dem < 1001:
        k = str(q.pop(0))
        if 2 * k.count("2") > len(k):
            dem += 1
            res.append(k)
        q.append(k + "0")
        q.append(k + "1")
        q.append(k + "2")


find_all()

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        print(res[i], end=" ")
    print()
