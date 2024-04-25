def buildheap(arr):
	non_leaf_node = len(arr) // 2 -1
	for i in range(non_leaf_node, -1, -1):
		heapify(arr, i)
		
def heapify(arr,i):
	largest = i
	left_child = 2 * i + 1
	right_child = 2 * i + 2
	
	if left_child < len(arr) and arr[left_child] > arr[largest]:
		largest  = left_child
	
	if right_child < len(arr) and arr[right_child] > arr[largest]:
		largest  = right_child
		  
	if largest !=i:
			arr[i], arr[largest] = arr[largest], arr[i]
			heapify(arr, largest)
			
def printheap(arr):
		print("Array Representation of heap is")
		for i in range(len(arr)):
			print(arr[i], end=" ")
		print()
			 
if __name__ == '__main__':
		arr= [2,4,5,8,6,9,3,12,45,98,78]
		buildheap(arr)
		printheap(arr)