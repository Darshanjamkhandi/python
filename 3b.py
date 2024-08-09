from math import *
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
if (a!=b and (a%2!=0 and b%2!=0)):
    a,b=b,a
    print("a : ",a)
    print("b : ",b)
elif (a!=b and (a%2==0 and b%2==0)):
    if(a>b):
        print(a)
    else:
        print(b)
else:
    print(factorial(a))
    print(factorial(b))