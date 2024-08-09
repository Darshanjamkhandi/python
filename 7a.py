n=input("Enter the string : ")
if n.isalpha():
    if n.startswith("t"):
        print("True")
    else:
        print("False")
elif n.isdigit():
    print(n[::-1])