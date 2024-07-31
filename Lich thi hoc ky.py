from datetime import datetime


class MH:
    def __init__(self, id, name) -> None:
        self.id, self.name = id, name
        pass


class LT:
    def __init__(self, stt, mon, ngay, gio, ca) -> None:
        self.id = "T" + "{:03d}".format(stt)
        self.mon = mon
        self.tg = " ".join([ngay, gio])
        self.ca = ca

    def __str__(self) -> str:
        return f"{self.id} {self.mon.id} {self.mon.name} {self.tg} {self.ca}"

    def __lt__(self, other):
        n1 = datetime.strptime(self.tg, "%d/%m/%Y %H:%M")
        n2 = datetime.strptime(other.tg, "%d/%m/%Y %H:%M")
        if n1 == n2:
            return self.mon.id < other.mon.id
        return n1 < n2


if __name__ == "__main__":
    n, m = map(int, input().split())
    mon = []
    for i in range(n):
        mon.append(MH(input(), input()))
    l = []
    for i in range(1, m + 1):
        mon_id, ngay, gio, ca = input().split()
        for j in mon:
            if j.id == mon_id:
                l.append(LT(i, j, ngay, gio, ca))
                break
    l.sort()
    for i in l:
        print(i)

"""
2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
"""
