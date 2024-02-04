
class Rectangle:
    def __init__(self, d, r, color):
        self.cv = (d+r)*2
        self.dt = d*r
        self.c = color.title()
    def perimeter(self):
        return self.cv
    def area(self):
        return self.dt
    def color(self):
        return self.c
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")