
t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()
    print("Test {}:".format(i+1), end=' ')
    if sorted(s1) == sorted(s2):
        print("YES")
    else: print("NO")

"""
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
"""