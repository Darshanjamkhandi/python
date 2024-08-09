a=int(input("Enter the number : "))
x=a
while(True):
    b=int(input("Enter the number : "))
    if(b==-1):
        break
    else:
        x=x*b
        print(x)
        x=b