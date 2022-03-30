def binary_search_first(numbers, target):
# your code here
    low = 0
    high = len(numbers) - 1
    #remove equal sign to exit loop while low move to same index of high
    while high > low:
        mid_index = (low + high) // 2
        # add equal sign to include the match condition
        if target <= numbers[mid_index]:
            high = mid_index
        else:
            low = mid_index + 1
    return low


print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
# should print 1 (the index of the target number ‘2’)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
# should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))
# should print 2 (since it can’t find number 3, return the index of ‘the smallest number
# larger then 3', that is, the index of the ‘first’ number 5)