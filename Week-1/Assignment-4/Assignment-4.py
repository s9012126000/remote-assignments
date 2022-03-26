def binary_search_position(numbers, target):
# your code here
    low = 0
    high = len(numbers)
    mid_index = (low+high)//2
    while numbers[mid_index] != target:
        if target > numbers[mid_index]:
            low = mid_index
            mid_index = (low+high)//2
        else:
            high = mid_index - 1
            mid_index = (low + high) // 2
    return mid_index

print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3