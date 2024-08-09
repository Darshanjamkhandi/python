l=[(10,20,40),(40,50,60),(70,80,90)]
li=[]
for i in l:
    li.append(list(i))
print(li)
for i in range(len(li)):
    li[i][2]=100
print(li)
l1=[]
for i in li:
    l1.append(tuple(i))
print(l1)