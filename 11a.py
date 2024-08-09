s=input("Enter the string : ")
a=s[:len(s)//2:]
b=s[len(s)//2::]
c=s[-1::-1]
if a==b and s==c:
    print("Symmetric and palindrome")
elif a==b and s!=c:
    print("Symmetric and not palindrome")
elif a!=b and s==c:
   print(" Not Symmetric and palindrome") 
else:
    print(" Not Symmetric and not palindrome")
