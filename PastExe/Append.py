a=[12,3,4,5,6,7,8,9,2,14]
b=[1,2,3,3,3,3,3,3,3,3]
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
        print(c)
