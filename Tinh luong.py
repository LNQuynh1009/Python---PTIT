d = [[10, 12, 14, 20], [10, 11, 13, 16], [9, 10, 12, 14], [8, 9, 11, 13]]


class P:
    def __init__(self, id, name) -> None:
        self.id, self.name = id, name
        pass


class NV:
    def __init__(self, id, name, luong, ngay, a) -> None:
        self.id, self.name = id, name
        nhom = id[0]
        nam = int(id[1:3])
        phong = id[3:]
        self.pb = ""
        for i in a:
            if i.id == phong:
                self.pb = i.name
                break
        c, j = 0, 0
        if nhom == "A":
            c = 0
        elif nhom == "B":
            c = 1
        elif nhom == "C":
            c = 2
        else:
            c = 3
        if nam in range(1, 4):
            j = 0
        elif nam in range(4, 9):
            j = 1
        elif nam in range(9, 16):
            j = 2
        else:
            j = 3
        self.luong = luong * ngay * d[c][j] * 1000
        pass

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.pb} {self.luong}"
        pass


if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(t):
        tmp = input().split()
        x = tmp[0]
        y = " ".join(tmp[1:])
        a.append(P(x, y))
    n = int(input())
    l = []
    for i in range(n):
        l.append(NV(input(), input(), int(input()), int(input()), a))

    for i in l:
        print(i)

"""
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
"""
