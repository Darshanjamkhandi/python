from math import *
n=int(input("Enter the number to find its sine value : "))
x=int(input("Enter the x value : "))
sign=-1
sum=1
p=2
for i in range(n):
    sum=sum+((x**p)/factorial(p)*sign)
    p=p+2
    sign=sign*-1
print(sum)