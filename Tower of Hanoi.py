
def solve(n, start, end, aux):
    if n == 1:
        print(start,"->", end)
        return
    solve(n-1, start, aux, end)
    print(start,"->", end)
    solve(n-1, aux, end, start)

n = int(input())
solve(n, "A", "C", "B")