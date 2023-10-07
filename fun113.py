n = int(input("Enter a six digit number: "))
a = 0
c = 1
if(n > 99999):
    while n > 0:
     b = n % 10
    if(b % 2 == 0 ):
     a += b
    else:
      c *= b
    n//=10
    print("Sum of even digits: ", a)
    print("Product of odd digits ", c)
else:
    print("Not a six digit number")