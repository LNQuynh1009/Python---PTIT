
res = []

def generate(i, s, na, nb, nc):
    if na>0 and na <= nb and nb <= nc:
        res.append(s)
    if i == n:
        return
    i+=1
    generate(i, s+'A', na+1, nb, nc)
    generate(i, s+'B', na, nb+1, nc)
    generate(i, s + 'C', na, nb, nc+1)

n = int(input())

generate(0, "", 0, 0, 0)

for i in sorted(res, key=lambda x: len(x)):
    print(i)