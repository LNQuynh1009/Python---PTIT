from itertools import permutations

t = int(input())

while t > 0:
    n = int(input())
    a = [i for i in range(1, n + 1)]
    res = permutations(a)
    res = list(res)
    print(len(res))
    res = res[::-1]
    for i in res:
        for j in i:
            print(j, end="")
        print(end=" ")
    print()
    t -= 1
