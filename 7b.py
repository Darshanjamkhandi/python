n=input("Enter the number : ")
flag=0
for i in range(len(n)):
    if i==0:
        if n[0]=='0':
            flag=0
        else:
            flag=0
    else:
        if n[i]=='0':
            flag=1
            break
        else:
            flag=0
if flag==1:
    print(int(n)," is a duck number")
else:
    print(int(n)," is not a duck number")