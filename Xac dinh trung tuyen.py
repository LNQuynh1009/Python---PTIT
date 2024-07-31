class GV:
    def __init__(self, stt, name, khoi, tin, cm) -> None:
        self.id = "GV" + "{:02d}".format(stt)
        self.name = name
        if khoi[0] == "A":
            self.mon = "TOAN"
        elif khoi[0] == "B":
            self.mon = "LY"
        else:
            self.mon = "HOA"
        tmp = tin * 2 + cm
        if khoi[1] == "1":
            tmp += 2.0
        elif khoi[1] == "2":
            tmp += 1.5
        elif khoi[1] == "3":
            tmp += 1.0
        else:
            tmp += 0.0
        self.diem = tmp
        if self.diem >= 18:
            self.status = "TRUNG TUYEN"
        else:
            self.status = "LOAI"
        pass

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.mon} {self.diem} {self.status}"
        pass


if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(GV(i, input(), input(), float(input()), float(input())))

    a.sort(key=lambda x: -x.diem)
    for i in a:
        print(i)

"""
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
"""
