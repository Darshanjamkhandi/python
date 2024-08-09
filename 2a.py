a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=input("Enter your choice\nA-bitwise\nB-aithmetic\n")
if c=='A':
    g=int(input("Enter your choice\n1-AND\n2-OR\n3-EXOR\n"))
    if g==1:
        res=a and b
        print(bin(int(res)))
    elif g==2:
        res=a or b
        print(bin(int(res)))
    elif g==3:
        res=a^b
        print(bin(int(res)))
elif c=='B':
    h=int(input("Enter your choice\n1-add\n2-sub\n3-multi\n4-div\n"))
    if h==1:
        res=a+b
        print(res)
    elif h==2:
        res=a-b
        print(res)
    elif h==3:
        res=a*b
        print(res)
    elif h==4:
        res=a/B
        print(res)