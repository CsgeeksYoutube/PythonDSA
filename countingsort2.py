def counting_sort(arr):
    low = min(arr)
    print(low)
    high = max(arr)
    k = high - low + 1
    print(k)

    count = [0] * k
    print(count)

    for num in arr:
        count[num - low] += 1
    print(count)


    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + low] * count[i])

    return sorted_arr

arr = [4, 2, 2, 18, 3, 8, 3, 5, 3, 7, 0, 1, 2, 6, 4, 3, 3, 0, 1,-14]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
