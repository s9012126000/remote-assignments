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
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
print(binary_search_position([1, 2, 5, 6, 7], 7)) # should print 4
print(binary_search_position([1, 2, 5, 6, 7, 8, 11, 15, 19, 31], 19)) # should print 8
print(binary_search_position([1, 2, 5, 6, 7, 8, 11, 15, 19, 31], 31)) # should print 9
print(binary_search_position([1, 2, 5, 6, 7, 8, 11, 15, 19, 31, 51], 31)) # should print 9
print(binary_search_position([1, 2, 5, 6, 7, 8, 11, 15, 19, 31, 51], 51)) # should print 10
print(binary_search_position([1, 2, 5, 6, 7, 8, 11, 15, 19, 31, 51], 100)) # should print -1