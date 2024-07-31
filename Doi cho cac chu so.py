for _ in range(int(input())):
    s = input()
    n = len(s) - 1
    while s[n] >= s[n - 1] and n > 0:
        n -= 1
    if n == 0 or (n == 1 and s[1] == "0"):
        print(-1)
        continue
    l = n - 1
    r = len(s) - 1
    while s[l] <= s[r] or s[r] == s[r - 1]:
        r -= 1
    print(s[:l] + s[r] + s[l + 1 : r] + s[l] + s[r + 1 :])

"""
4
354
999
100
11101
"""
