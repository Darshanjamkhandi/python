s=input("Enter the string : ")
ss=input("Enter the sub string : ")
st=""
if ss in s:
    sss=input("Enter the new string : ")
    a=s.replace(ss,sss)
    print(a)
else:
    b=s[:(len(s)//2)+1]
    c=s[(len(s)//2):len(s)]
    st=st+b+ss+c
    print(st)

