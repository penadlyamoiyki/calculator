def slove(num1, num2, operation):
      try:
       num1 = int(num1)
       num2 = int(num2)
      except:
          num3 = num1 + " " + operation + " " +num2
          return num3

      x = "total: "
      num3 = ""
      print(num1)
      print(num2)
      print(operation)
      if operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "!" and operation != "#":
            num3 = "operation not found"

      if operation == "+":
        num3 = plus(num1, num2)

      elif operation == "-":
        num3 = minus(num1, num2)

      elif operation == "*":
        num3 = mult(num1, num2)

      elif operation == "/":
        num3 = division(num1, num2)

      elif operation == "!":
        num3 = faktor(num1)

      elif operation == "#":
        num3 = root(num1)

      if num3 != "" and num3 != "root can`t be minus":
            print(x + str(num3))
      elif num3 == "root can`t be minus":
            print(num3)
      return num3

def division(num1, num2):
    num3=""
    if num2 == 0:
        print("cant division by zero")
    else:
     num3=num1/num2
    return num3

def mult(num1, num2):
    num3 = num1 * num2
    return num3

def plus(num1, num2):
    num3 = num1 + num2
    return num3

def minus(num1, num2):
    num3 = num1 - num2
    return num3

def faktor(num1):
    i = 0
    c = 1
    while i < num1:
        i += 1
        num3 = i * c
        c = num3
    return num3

def root(num1):
    if num1 >= 0:
        num3 = num1 ** 0.5
        return num3
    elif num1 < 0:
        num3 = ("root can`t be minus")
        return num3
