def bucketSort(array):
    num_buckets = len(array)
    buckets = [[] for _ in range(num_buckets)]

    for element in array:
        index = int(num_buckets * element)
        print(index)
        buckets[index].append(element)
        print(buckets)

    
        
    for i in range(num_buckets):
        insertionSort(buckets[i])
    
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

def insertionSort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

input_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51,0.01]
sorted_result = bucketSort(input_array)
print("Sorted Array:", sorted_result)
