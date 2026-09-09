"""
write a program to display product of number from  1 to n
"""

n = int(input("Enter upper limit:"))

product = 1

for i in range(1,n+1):

    product*=i
    i+=1

print(f"product = {product}")