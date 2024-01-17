
tc = int(input())

while tc > 0:
    [n, t] = input().split()
    n, t = int(n), int(t)
    zodiac = ""
    if t == 1:
        if n <= 19: zodiac = "Ma Ket"
        else: zodiac = "Bao Binh"
    elif t == 2:
        if n <= 18: zodiac = "Bao Binh"
        else: zodiac = "Song Ngu"
    elif t == 3:
        if n <= 20: zodiac = "Song Ngu"
        else: zodiac = "Bach Duong"
    elif t == 4:
        if n <= 19: zodiac = "Bach Duong"
        else: zodiac = "Kim Nguu"
    elif t == 5:
        if n <= 20: zodiac = "Kim Nguu"
        else: zodiac = "Song Tu"
    elif t == 6:
        if n <= 20: zodiac = "Song Tu"
        else: zodiac = "Cu Giai"
    elif t == 7:
        if n <= 22: zodiac = "Cu Giai"
        else: zodiac = "Su Tu"
    elif t == 8:
        if n <= 22: zodiac = "Su Tu"
        else: zodiac = "Xu Nu"
    elif t == 9:
        if n <= 22: zodiac = "Xu Nu"
        else: zodiac = "Thien Binh"
    elif t == 10:
        if n <= 22: zodiac = "Thien Binh"
        else: zodiac = "Thien Yet"
    elif t == 11:
        if(n <= 22): zodiac = "Thien Yet"
        else: zodiac = "Nhan Ma"
    else:
        if n <= 21: zodiac = "Nhan Ma"
        else: zodiac = "Ma Ket"
    print(zodiac)
    tc -= 1

"""
2
5 5
30 7
"""