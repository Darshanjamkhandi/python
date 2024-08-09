from math import *
s=input("Enter the input seperated by comma : ")
c=50
h=30
d=s.split(",")
for i in d:
    a=int(i)
    q=sqrt((2*c*a)/h)
    print(int(q))