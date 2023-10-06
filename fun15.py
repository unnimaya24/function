
for i in range(1,10):
        if(i%2!=0):
            for j in range (0,i+1):
                print (j,end="")
            print()
        else:
            for k in range (i+1,0,-1):
                print(k,end="")
            print() 
        for p in range (0,i+1):
                    print('*',end="")
        print()   
   