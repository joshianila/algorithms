def binarySearch(arr,ele):
	low = 0
	high = len(arr)-1

	while low <= high:
		mid = (low+high)//2
		if arr[mid] == ele:
			return mid
		if arr[mid] < ele:
			low = mid+1
		else:
			high = mid-1
	return None
arr = [1,3,6,8,9,10]
print(binarySearch(arr,11))