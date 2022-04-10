def twoSum(nums, target):
    for i in range(len(nums)):
        num2 = target - nums[i]
        if num2 in nums and nums.index(num2) != i:
            return i, nums.index(num2)
        
# find another value with subtraction
# find index of another value by index()
# replace nested for loop with single for loop
# O(n^2) -> O(n)

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))