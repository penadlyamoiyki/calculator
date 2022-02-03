def division(num):
    num3=""
    if num[1] == 0:
        print("cant division by zero")
    else:
     num3=num[0]/num[1]
    return num3

def mult(num):
    num3 = num[0] * num[1]
    return num3

def plus(num):
    num3 = num[0]+num[1]
    return num3

def minus(num):
    num3 = num[0]-num[1]
    return num3

def faktor(num):
    i = 0
    c = 1
    while i < num[0]:
        i += 1
        num3 = i * c
        c = num3
        print(num3)
    return num3