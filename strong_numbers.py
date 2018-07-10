import math


def strong_num(number):
    i = 0
    number = str(number)
    a = 0
    b = 0
    ret = ''
    while i < len(number):
        a = int(math.factorial(int(number[i])))
        print(str(a) + "= a")
        b = a + b
        print(str(b) + "= b")
        print(str(i) + "= i")
        i = i + 1
    print(b)
    if b == int(number):
        ret = ret + "STRONG!!!!"
    else:
        ret = ret + "Not Strong !!"
    return ret
