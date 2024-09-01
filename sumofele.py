def sum_of_ele(arr):
    total_sum = 0
    for ele in arr: 
        total_sum += ele
    return total_sum


array = [1, 2, 3, 4, 5]
total_sum = sum_of_ele(array)
print(f"The sum of elements in the array is: {total_sum}")
