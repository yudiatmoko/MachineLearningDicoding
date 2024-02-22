import array

# Array Library
x = array.array("i", [1,2,3])
print(x)

# Array List Comprehension
var_arr = [0 for i in range(10)]
for i in range(10):
    var_arr[i] = i
print(var_arr)
print(var_arr[2])

# Sequencial
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")

# Two Pointer Algorithm
varArr = [3, 7, 1, 89, 0]
left_pointer = varArr[0]

for i in range(1, len(varArr)):
    right_pointer = varArr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)

var_array = [i for i in range(101)]
leftPointer = var_array[0]

for i in range(1, len(var_array)):
    rightPointer = var_array[i]
    jumlah = leftPointer + rightPointer
    leftPointer = jumlah
result = leftPointer / len(var_array)
print(result)
