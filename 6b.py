n=int(input("Enter N numbers : "))
x=int(input("Enter the number : "))
a=x
for i in range(n-1):
    b=int(input("Enter the number : "))
    avg=(a+b)/2
    print(avg)
    a=b