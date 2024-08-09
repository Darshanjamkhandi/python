n=int(input("Enter the number : "))
s=0
for i in range(n):
    s+=i
    if s==n:
        print(n,"is perfect number")
        break
else:
    print(n,"is not perfect number")

