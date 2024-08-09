n=int(input("Enter the N : "))
sum=1
for i in range(2,n+1):
    sum=sum+1/i
print(sum)
s=0
for i in range(1,n+1):
    s=s+((i**i)/i)
print(s)