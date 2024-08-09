l=[1,2,1,2,4,2,1,5,4,6,2,1,4,5,6,7,8]
dic={}
for i in l:
    if i not in dic:
        dic[i]=l.count(i)
print(dic)