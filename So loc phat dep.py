
def loc(s):
    for i in s:
        if i!='6' and i != '8':
            return False
    return True

def dep(s):
    return s.endswith('6') or s.endswith('68') or s.endswith('688')

s = input()
if loc(s) and dep(s):
    print("YES")
else: print("NO")