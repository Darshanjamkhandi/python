n=input("Enter the number : ")
flag=0
a=int(n)
for i in n:
    if a%int(i)==0:
        flag=1
    else:
        flag=0
        break
if flag==1:
    print(a,"is nude number")
else:
    print(a,"is  not nude number")   