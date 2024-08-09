l1=[1,2,3,4]
l2=[4,3,2,1]
if l1[0]==l2[len(l2)-1] and l2[0]==l1[len(l1)-1]:
    print("Lists are circular")
else:
    print("Lists are not circular")