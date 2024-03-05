import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
t = int(input())

while t > 0:
    ip = input()
    if re.search(regex, ip):
        print("YES")
    else:
        print("NO")
    t -= 1

"""
2
192.168.1.1
256.255.255.255
"""
