nums=[2,3,4,5,6]
nums=[2,4,8,3]
def even_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if (product%2)==0:
           print(product,"is even")
        else:
          sum=nums[i]+nums[j]
        if(sum%2)==0:
          print(sum,"is odd")
             
        














