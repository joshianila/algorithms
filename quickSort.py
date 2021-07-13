def quickSort(arr):
	if len(arr)<2:
		return arr
	pivot = arr[0]
	lesser = [i for i in arr[1:] if i<=pivot]
	greater = [i for i in arr[1:] if i > pivot]
	return quickSort(lesser) + [pivot] + quickSort(greater)
arr = [4,1,6,2,8,5]
print(quickSort(arr))