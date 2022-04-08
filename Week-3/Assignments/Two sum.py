def twoSum(nums, target):
    table = {}
    for i in range(len(nums)):
        table[nums[i]] = i  # create hash table
    for i in range(len(nums)):
        if target - nums[i] in table and table[target - nums[i]] != i:
            return [i, table[target - nums[i]]]
        
# using hash table to save the index of nums data
# find another value with subtraction
# call the index from hash table
# replace nested for loop with single for loop
# O(n^2) -> O(n)

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))