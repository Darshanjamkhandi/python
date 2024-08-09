l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
li=[]
for i in l:
    li.append(list(i))
print(li)
for i in range(len(li)):
    for j in range(len(li)-i-1):
        if li[j][-1]>li[j+1][-1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
    