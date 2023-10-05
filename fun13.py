n=[2,3,4,5,6]
def find_pairs(nums, target_val):
    nums_set = set(nums)
    pairs = []
    for n in nums_set:
        complement = target_val - n
        if complement in nums_set:
            pairs.append({n, complement})
    return pairs