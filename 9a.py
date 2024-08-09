from math import *
x=int(input("Enter the x coordinate of circle : "))
y=int(input("Enter the y coordinate of circle : "))
x1=int(input("Enter the x coordinate of point : "))
y1=int(input("Enter the y coordinate of point : "))
r=int(input("Enter the radius : "))
dis=sqrt(((x1-x)**2)+((y1-y)**2))
if dis<r:
    print("point lies in circle")
elif dis==r:
    print("point lies on circumference circle")
else:
    print("point lies outside circle")