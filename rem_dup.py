def rem_dup(arr):
     unique_ele = []
     for ele in arr:
         if ele not in unique_ele:
             unique_ele.append(ele)
     return unique_ele
     
print(rem_dup([1,2,2,3,4,4,5]))