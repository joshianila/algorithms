def findMin(arr):
	minValue = float('inf')
	for i in arr:
		if i < minValue:
			minValue = i
	return minValue

print(findMin([4,1,9,3,5,8]))