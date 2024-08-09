n=int(input("Enter the no. of lines : "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()