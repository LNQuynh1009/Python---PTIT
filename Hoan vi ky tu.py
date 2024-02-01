from itertools import permutations
s = input()

a = [i for i in s]
res = list(permutations(a))
for i in res:
    for j in i:
        print(j, end='')
    print()
