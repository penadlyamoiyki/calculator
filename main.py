import sys
import modul
numbers = []
num3 = ""
x = "total: "
numbers.append(int(input("number 1: ")))
operation = input("operation: ")
if operation == "!":
    print("")
else:
    numbers.append(int(input("number 2: ")))

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

else:
    print("operation not found")

if num3 != "":
    print(x + str(num3))
#  comment
