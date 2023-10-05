n = int(input ("Enter the number : "))  
x = 0    
y= 1 

for i in n: 
    print(x, end = " ")         
    z = x+y                   
    x = y               
    y = z
    