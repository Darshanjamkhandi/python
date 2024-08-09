s1=input("Enter the string 1 : ")
s2=input("Enter the string 2 : ")
a=s1.split(" ")
b=s2.split(" ")
l=[]
for i in a:
    if i not in b:
        l.append(i)
for i in b:
    if i not in a:
        l.append(i)
c=" ".join(l)
print(c)