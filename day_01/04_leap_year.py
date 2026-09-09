"""
write a program to chk year is leap year or not

"""

year = int(input("Enter a number:"))

if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
    print("Leap year")

else:
    print("Not a leap year")