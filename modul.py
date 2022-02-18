def slove(num1, num2, operation):
      x = "total: "
      num3 = ""
      print(num1)
      print(num2)
      print(operation)
    #operation = "+"
    #num1 = (int(input("number 1: ")))
    #while operation != "":
      #operation = input("operation: ")
      if operation == "" and num1 == "0" and num2 == "0":
          print("da")
      if operation == "!" or operation == "#":
            print("")
      else: # operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "!" and operation != "#":
            print("operation not found")
      #else:
          # num2 = (int(input("number 2: ")))

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

      else:
        print("print right operation")

      if num3 != "" and num3 != "root can`t be minus":
            print(x + str(num3))
      elif num3 == "root can`t be minus":
            print(num3)
            num3 = 0
      num1 = num3
    
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
