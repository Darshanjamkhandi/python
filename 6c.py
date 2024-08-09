n=input("Enter the number : ")
a=int(n)
s=0
for i in n:
    s+=(int(i)**3)
if s==a:
    print(a,"is amstrong number")
else:
    print(a,"is not amstrong number")