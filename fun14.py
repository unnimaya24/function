n=['2','3','4','5','6']
for i in range(len(n)-1):
        for j in range (i+1,len(n)):
            if(i % 2 == 0):
             n*= i
             pair=(n[i],n[j])
print(n)            
            
        