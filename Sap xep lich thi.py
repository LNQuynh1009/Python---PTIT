from datetime import datetime


class Mon:
    def __init__(self, id, name, ht) -> None:
        self.id, self.name, self.ht = id, name, ht
        pass


class Ca:
    def __init__(self, stt, ngay, gio, phong) -> None:
        self.id = "C" + "{:03d}".format(stt)
        self.ngay, self.gio = ngay, gio
        self.time = datetime.strptime(ngay + " " + gio, "%d/%m/%Y %H:%M")
        self.phong = phong
        pass


class Lich:
    def __init__(self, ca, mon, nhom, sv, m, c) -> None:
        for i in c:
            if i.id == ca:
                self.section = i
                break
        for j in m:
            if j.id == mon:
                self.subject = j
                break
        self.nhom, self.sv = nhom, sv
        pass

    def __str__(self) -> str:
        return f"{str(self.section.ngay)} {self.section.gio} {self.section.phong} {self.subject.name} {self.nhom} {self.sv}"
        pass


if __name__ == "__main__":
    m = []
    with open("MONTHI.in", "r") as f:
        for _ in range(int(f.readline().strip())):
            m.append(
                Mon(f.readline().strip(), f.readline().strip(), f.readline().strip())
            )
    c = []
    with open("CATHI.in", "r") as f:
        for _ in range(1, int(f.readline().strip()) + 1):
            c.append(
                Ca(_, f.readline().strip(), f.readline().strip(), f.readline().strip())
            )
    l = []
    with open("LICHTHI.in", "r") as f:
        for _ in range(int(f.readline().strip())):
            ca, mon, nhom, sv = f.readline().strip().split()
            l.append(Lich(ca, mon, nhom, sv, m, c))
    l.sort(key=lambda x: x.section.time)
    for i in l:
        print(i)
