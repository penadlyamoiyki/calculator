import sys
import modul
numbers = [0, 0]
num3 = ""
x = "total: "
operation = "+"
numbers[0] = (int(input("number 1: ")))
while operation != "":
 operation = input("operation: ")
 if operation == "!" or operation == "#":
    print("")
 elif operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "!" and operation != "#":
     print("operation not found")
 else:
   numbers[1] = (int(input("number 2: ")))

 if operation == "+":
    num3 = modul.plus(numbers)

 elif operation == "-":
    num3 = modul.minus(numbers)

 elif operation == "*":
    num3 = modul.mult(numbers)

 elif operation == "/":
    num3 = modul.division(numbers)

 elif operation == "!":
    num3 = modul.faktor(numbers)

 elif operation == "#":
     num3 = modul.root(numbers)

 else:
  print("print right operation")

 if num3 != "":
    print(x + str(num3))

 numbers[0] = num3
