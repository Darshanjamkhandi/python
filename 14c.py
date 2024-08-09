s="14,625,498.002"
st=""
for i in s:
    if i==",":
        st=st+"."
    elif i==".":
        st=st+","
    else:
        st=st+i
print(st)