
s = input()
bin = [("", '')]*8

bin[0] = ("000", '0')
bin[1] = ("001", '1')
bin[2] = ("010", '2')
bin[3] = ("011", '3')
bin[4] = ("100", '4')
bin[5] = ("101", '5')
bin[6] = ("110", '6')
bin[7] = ("111", '7')

while len(s)%3 != 0:
    s = "0"+s

i = len(s)-1
while i > 0:
    tmp = s[i-2:i+1]
    for j in bin:
        if tmp == j[0]:
            s = s[:i-2] + j[1] + s[i+1:]
    i -= 3
print(s)

"""
bin_oct_map["000"] = '0'
bin_oct_map["001"] = '1'
bin_oct_map["010"] = '2'
bin_oct_map["011"] = '3'
bin_oct_map["100"] = '4'
bin_oct_map["101"] = '5'
bin_oct_map["110"] = '6'
bin_oct_map["111"] = '7'
"""