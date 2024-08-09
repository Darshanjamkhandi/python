s=input("Enter string with spaces : ")
a=s.split(" ")
l=[]
for i in a:
    a=i[0].upper()
    b=i[-1].upper()
    c=a+i[1:len(i)-1:]+b
    l.append(c)
aa=" ".join(l)
print(aa)