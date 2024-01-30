class Student:
    def __init__(self, idx, Name, p):
        self.ID = "HS" + "{:02d}".format(idx)
        self.Name = Name
        self.diemTB = p[0] * 2.0 + p[1] * 2.0
        for i in range(2, 10):
            self.diemTB += p[i]
        self.diemTB = self.diemTB/12
        self.diemTB = round(self.diemTB*100+1)/100
        if self.diemTB >= 9.0:
            self.xepLoai = "XUAT SAC"
        elif self.diemTB >= 8.0:
            self.xepLoai = "GIOI"
        elif self.diemTB >= 7.0:
            self.xepLoai = "KHA"
        elif self.diemTB >= 5.0:
            self.xepLoai = "TB"
        else:
            self.xepLoai = "YEU"
    def getInfo(self):
        return "{} {} {:.1f} {}".format(self.ID, self.Name, round(self.diemTB, 2), self.xepLoai)

def cmp(a):
    return (a.diemTB, (-1) * a.ID)

List = []

for i in range(int(input())):
    List.append(Student(i + 1, input(), list(map(float, input().split()))))

List.sort(key=cmp, reverse=True)

for i in List:
    print(i.getInfo())

"""
3
Luu Thuy Nhi
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""