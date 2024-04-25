def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    print(count)
    for num in arr:
        count[num] += 1

    print(count)
    

    sorted_arr = [0] * len(arr)
    
    k = 0
    for i in range (0, max(arr)+1):
        if count[i]> 0:
            for j in range(0,count[i]):
                sorted_arr[k] = i
                k=k+1
    return sorted_arr


# Example usage:
arr = [4, 2, 2, 18, 3,8 ,3,5,3,7,0,1,2,6,4,3,3, 0,1,]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
