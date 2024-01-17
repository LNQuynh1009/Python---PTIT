
t = int(input())

def factorial(n):
    return 1 if(n == 0 or n == 1) else n*factorial(n-1)

while t > 0:
    num = input()
    cnt = 0
    for i in num:
        cnt += factorial(int(i))
    if (int(num) == cnt):
        print("Yes")
    else:
        print("No")
    t -= 1