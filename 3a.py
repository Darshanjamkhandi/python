from math import *
n=int(input("Enter the number to find its sine value : "))
x=int(input("Enter the x value : "))
sign=1
sum=0
p=1
for i in range(n):
    sum=sum+((x**p)/factorial(p)*sign)
    p+=2
    sign*=-1
print(sum)