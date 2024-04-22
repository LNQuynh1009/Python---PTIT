from datetime import datetime

class CaThi:
    stt = 1
    def __init__(self, ngayThi, gioThi, phongThi) -> None:
        self.ma = "C%03d" %(CaThi.stt)
        CaThi.stt+=1
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.phongThi = phongThi
        self.time = datetime.strptime(ngayThi+' '+gioThi,"%d/%m/%Y %H:%M")
        pass
    def getInfo(self):
        print("{} {} {} {}".format(self.ma,self.ngayThi, self.gioThi, self.phongThi))


with open('CATHI.in','r') as f:
    dsCaThi = [CaThi(f.readline().strip(), f.readline().strip(), f.readline().strip()) for _ in range(int(f.readline()))]

dsCaThi.sort(key=lambda x: (x.time, x.ma))

for caThi in dsCaThi:
    caThi.getInfo()