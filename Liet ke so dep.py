
d = ['0', '2', '4', '6', '8']
def check(n):
    if str(n) != str(n)[::-1]:
        return False
    for i in str(n):
        if i not in d:
            return False
    if len(str(n))%2 != 0:
        return False
    return True

t = int(input())

while t > 0:
    n = int(input())
    for i in range(22, n, 2):
        if check(i):
            print(i, end=" ")
    print()
    t -= 1