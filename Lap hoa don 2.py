from datetime import datetime


class KH:
    def __init__(self, stt, name, room, nhan, tra, dvu) -> None:
        self.id = "KH" + "{:02d}".format(stt)
        self.name = name
        self.room = room
        d0 = datetime.strptime(nhan, "%d/%m/%Y")
        d1 = datetime.strptime(tra, "%d/%m/%Y")
        delta = d1 - d0
        self.ngay = delta.days + 1
        if room[0] == "1":
            self.tien = 25 * self.ngay + dvu
        elif room[0] == "2":
            self.tien = 34 * self.ngay + dvu
        elif room[0] == "3":
            self.tien = 50 * self.ngay + dvu
        else:
            self.tien = 80 * self.ngay + dvu

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.room} {self.ngay} {self.tien}"


if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(
            KH(
                i,
                input().strip(),
                input().strip(),
                input().strip(),
                input().strip(),
                int(input().strip()),
            )
        )

    a.sort(key=lambda x: -x.tien)
    for i in a:
        print(i)

"""
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
"""
