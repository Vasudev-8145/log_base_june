

"""
write a program to print largest of three numbers

"""

num1 = int(input("Enter a num1:"))
num2 = int(input("Enter a num2:"))
num3 = int(input("Enter a num3:"))

if num1>num2 and num1>num3:
    print(f"{num1} is greatest")

elif num2>num1 and num2>num3:
    print(f"{num2} is greatest")

elif num3>num1 and num3>num1:
    print(f"{num3} is greatest")