def find_max(arr):
    max_ele = arr[0]
    for ele in arr:
        if ele > max_ele:
            max_ele = ele
    return max_ele
    
print(find_max([1,4,5,3,6,2]))