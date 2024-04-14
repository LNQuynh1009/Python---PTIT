n = input()

while len(n) > 1:
    n1 = int(n[: int(len(n) / 2)])
    n2 = int(n[int(len(n) / 2) :])
    tmp = n1 + n2
    n = str(tmp)
    print(n)
