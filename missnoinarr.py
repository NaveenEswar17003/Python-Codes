def missingnoinarr(arr):
    n = len(arr)+1
    tot_sum = n*(n+1)//2
    act_sum = sum(arr)
    return tot_sum - act_sum
    
print(missingnoinarr([1,2,3,4,5]))