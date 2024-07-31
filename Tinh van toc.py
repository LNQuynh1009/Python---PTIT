class VDV:
    def __init__(self, name, dv, h) -> None:
        self.name, self.dv = name, dv
        tmp = (dv + " " + name).split()
        self.id = ""
        for i in tmp:
            self.id += i[0]
        g, p = map(int, h.split(":"))
        self.vt = 120 / ((g - 6) + p / 60)
        pass

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.dv} {round(self.vt)} Km/h"


if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(VDV(input(), input(), input()))

    a.sort(key=lambda x: -x.vt)

    for i in a:
        print(i)

"""
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
"""
