s=input("Enter the string : ")
a=0
if s.isalpha():
    if s.islower():
        print("lower")
    elif s.isupper():
        print("upper")
elif s.isdigit():
    for i in s:
        a+=int(i)
    print(a)
elif s.isalnum():
    pass
else:
    b=len(s)
    print(b)