
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    ans = []
    for i in range(n):
        while len(st) > 0 and a[i] >= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            ans.append(i+1)
        else: ans.append(i-st[-1])
        st.append(i)
    for i in ans:
        print(i, end=' ')
    print()
    t -= 1

"""
1
7
100 80 60 70 60 75 85
"""