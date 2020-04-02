def myComparator(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if (a == b) or (b == c) or (a == c):
        return True
    return False

print(myComparator(6,5,"5"))
