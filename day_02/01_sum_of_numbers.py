"""
write a program to display sum of number from  1 to n
"""

n = int(input("Enter upper limit:"))

sum = 0

for i in range(1,n+1):

    sum+=i
    i+=1

print(f"sum = {sum}")