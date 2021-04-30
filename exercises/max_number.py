print("Description: This program will find the biggest value of 2 numbers")

x = input("Please input first number: ")
y = input("Please input second number: ")

x = float(x)
y = float(y)

if x > y:
    max_number = x
    info = "First number is greater than second"
elif y > x:
    max_number = y
    info = "Second number is greater than first"
elif x == y:
    max_number = None
    info = "Numbers are even"
else:
    max_number = None
    info = "Unexpected behavior"

print(info)
if max_number:
    print("Greatest number value: " + str(max_number))
