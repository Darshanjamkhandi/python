x1=int(input("Enter x1 : "))
y1=int(input("Enter y1 : "))
x2=int(input("Enter x2 : "))
y2=int(input("Enter y2 : "))
x3=int(input("Enter x3 : "))
y3=int(input("Enter y3 : "))
s=((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2)))
if s==0:
    print("Points are collinear")
else:
    print("Points are not collinear")