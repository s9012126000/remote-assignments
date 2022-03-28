def binary_search_position(numbers, target):
# your code here
    low = 0
    high = len(numbers)-1
    while high >= low:
        mid_index = (low + high) // 2
        if target == numbers[mid_index]:
            return mid_index
        elif target > numbers[mid_index]:
            low = mid_index + 1
        else:
            high = mid_index - 1
    return -1

print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 2)) # should print 1
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
print(binary_search_position([1, 2, 5, 6, 7], 7)) # should print 4
print(binary_search_position([1, 2, 5, 6, 7, 11], 1)) # should print 0
print(binary_search_position([1, 2, 5, 6, 7, 11], 2)) # should print 1
print(binary_search_position([1, 2, 5, 6, 7, 11], 7)) # should print 4
print(binary_search_position([1, 2, 5, 6, 7, 11], 11)) # should print 5
print(binary_search_position([1, 2, 5, 6, 7, 11], 100)) # should print -1