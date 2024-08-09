from math import *
a=int(input("Enter the a value : "))
b=int(input("Enter the b value : "))
c=int(input("Enter the c value : "))
qd=b*b-(4*a*c)
if qd==0:
    print("Roots are real and equal\n")
    r1=-b/(2*a)
    print("Root1 and Root2 : ",r1)
elif qd>0:
    print("Roots are real and distinct\n")
    r1=(-b+sqrt(qd))/(2*a)
    r2=(-b-sqrt(qd))/(2*a)
    print("Root1 : ",r1)
    print("Root2 : ",r2)
else:
    print("Roots are distinct and imaginary\n")
    r=-b/(2*a)
    r1=(sqrt(abs(qd)))/(2*a)
    r2=(sqrt(abs(qd)))/(2*a)
    print("Root 1: ",complex(r,r1))
    print("Root 2: ",complex(r,r2))   