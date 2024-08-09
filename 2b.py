n=int(input("Enter the odd number : "))
for i in range(n):
    print("*",end=" ")
print()
for j in range((n//2)+1):
    for k in range(n//2):
        print(" ",end=" ")
    print("*")