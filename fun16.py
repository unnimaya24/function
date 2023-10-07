def findPair(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                
if __name__ == '__main__':
 
    nums = [3,8,12,7,6,10,21,15]
    target = 18
 
    findPair(nums, target)