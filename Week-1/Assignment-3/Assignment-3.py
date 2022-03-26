def find_max(numbers):
# your code here
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    
def find_position(numbers, target):
# your code here
    if target in numbers:
        for i in range(len(numbers)):
            if target == numbers[i]:
                return i
    else:
        return -1
        
print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1