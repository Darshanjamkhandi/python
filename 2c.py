n=int(input("Enter the number to find its fibonacci sequence : "))
f1=0
f2=1
for i in range(n):
    if i==0:
        print(f1,end="->")
    elif i==1:
        print(f2,end="->")
    else:
        if i==n-1:
            f3=f1+f2
            print(f3)
        else: 
            f3=f1+f2
            print(f3,end="->")
            f1,f2=f2,f3