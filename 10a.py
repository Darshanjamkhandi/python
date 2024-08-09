s=input("Enter the string : ")
if s.isalpha():
    a=len(s)
    print(a)
elif s.isdigit():
    a=len(s)
    print(a)
elif s.isalnum():
    pass
else:
    b=len(s)
    print(b)