a=['apple','banana','cherry','dates']
c=[]
for i in range (len(a)):
    for j in range(i,len(a)):
        for n in a[i]:
         if n in a[j]:
             pair=(a[i],a[j])
             c.append(pair)
             break
print(c)