def maxlen(a, n):
    cm, Max = 1, 0
    for i in range(0, n):
        if a[i] > Max:
            Max = a[i]
    i = 0
    while i < n - 1:
        count = 1
        if a[i] == a[i + 1] and a[i] == Max:
            for j in range(i + 1, n):
                if a[j] == Max:
                    count += 1
                    i += 1
                else:
                    break
            if count > cm:
                cm = count
        else:
            i += 1
        i += 1
    return cm


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(maxlen(a, n))

"""
5
5 1 6 7 2
"""
