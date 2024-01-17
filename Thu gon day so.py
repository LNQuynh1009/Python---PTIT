
n = int(input())
a = (list(map(int, input().split())))
st = []
for i in a:
    if(st == []):
        st.append(i)
    else:
        y = st.pop()
        if((i+y) % 2 != 0):
            st.append(y)
            st.append(i)
print(len(st))

"""
10
1 5 5 8 6 4 3 5 9 3
"""