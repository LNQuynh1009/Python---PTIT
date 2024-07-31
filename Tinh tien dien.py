class KH:
    def __init__(self, stt, name, line) -> None:
        self.id = "KH" + "{:02d}".format(stt)
        tmp = name.strip().split()
        self.name = ""
        for i in tmp:
            self.name += i.title() + " "
        loai, dau, cuoi = line
        dau = int(dau)
        cuoi = int(cuoi)
        if loai == "A":
            dm = 100
        elif loai == "B":
            dm = 500
        else:
            dm = 200
        dien = cuoi - dau
        if dien < dm:
            self.trong = dien * 450
            self.vuot = 0
            self.vat = 0
        else:
            self.trong = dm * 450
            self.vuot = (dien - dm) * 1000
            self.vat = self.vuot // 20
        self.tong = self.trong + self.vuot + self.vat
        pass

    def __str__(self) -> str:
        return f"{self.id} {self.name}{self.trong} {self.vuot} {self.vat} {self.tong}"


if __name__ == "__main__":
    t = int(input())
    a = []
    for i in range(1, t + 1):
        a.append(KH(i, input(), input().split()))
    a.sort(key=lambda x: -x.tong)
    for i in a:
        print(i)

"""
2
 nGuyEn Hong Ngat
C 200 278
 Chu thi    minh
A 120 160
"""
