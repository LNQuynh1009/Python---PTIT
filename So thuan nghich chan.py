
t = int(input())

def check(n):
    for i in n:
        if i != '2' and i != '4' and i != '8' and i != '6' and i != '0':
            return False
    for i in range(0, int(len(n)/2)):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

while t > 0:
    n = int(input())
    for i in range(22, n):
        if i % 11 == 0 and check(str(i)) and len(str(i)) % 2 == 0:
            print(i, end=' ')
    print()
    t -= 1