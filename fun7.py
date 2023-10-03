lv = int(input ("Please, Enter the Lowest Value: "))  
uv= int(input ("Please, Enter the Upper Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for num in range (lv, uv + 1):  
    if num > 1:  
        for i in range (2, num):  
            if (num% i) == 0:  
                break  
        else:  
            print (num)  