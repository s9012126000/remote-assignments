def count(input):
# your code here
    output = {}
    for letter in input:
        try:
            output[letter] += 1
        except KeyError:
            output[letter] = 1
    return output

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}




def group_by_key(input):
# your code here
    output = {}
    for i in range(len(input)):
        try:
            output[input[i]['key']] += input[i]['value']
        except KeyError:
            output[input[i]['key']] = input[i]['value']
    return output

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]

print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}