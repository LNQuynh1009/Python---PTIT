class team:
    def __init__(self, stt, id, name) -> None:
        self.ma = "Team" + "{:02d}".format(stt)
        self.id, self.name = id, name
        pass

    def __str__(self) -> str:
        return f"{self.ma} {self.id} {self.name}"
        pass


class SV:
    def __init__(self, stt, name, t) -> None:
        self.id = "C" + "{:03d}".format(stt)
        self.name = name
        self.t = t

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.t.id} {self.t.name}"
        pass


t = int(input())
Team = []
for i in range(1, t + 1):
    Team.append(team(i, input(), input()))

n = int(input())
l = []
for i in range(1, n + 1):
    ten = input()
    doi = input()
    for j in Team:
        if j.ma == doi:
            l.append(SV(i, ten, j))
            break

l.sort(key=lambda x: x.name)
for i in l:
    print(i)

"""
2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
"""
