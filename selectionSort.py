def selectionSort(arr):
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			if arr[j] < arr[i]:
				arr[i],arr[j] = arr[j],arr[i]
	return(arr)
arr = [9,4,6,7,1,3]
print(selectionSort(arr))