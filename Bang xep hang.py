
class Student:
    def __init__(self, name, sum, sub):
        self.name = name
        self.sum = sum
        self.sub = sub

def cmp(s1, s2):
    if s1.sum == s2.sum and s1.sub == s2.sub:
        t1 = s1.name.split()
        t2 = s2.name.split()
        return t1[len(t1)-1] > t2[len(t2)-1]
    if s1.sum == s2.sum:
        return s1.sub > s2.sub
    return s1.sum < s2.sum
a = []

n = int(input())
for i in range(0, n):
    ten = input()
    tong, submit = input().split()
    tong, submit = int(tong), int(submit)
    a.append(Student(ten, tong, submit))
for i in range(0, n-1):
    for j in range(i, n):
        if cmp(a[i], a[j]):
            a[i], a[j] = a[j], a[i]
for i in a:
    print(i.name, i.sum, i.sub)

"""
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
"""