s=input("Enter the string : ")
for i in s:
    if i.isalnum():
        pass
    else:
        a=s.replace(i,"")
print(a)