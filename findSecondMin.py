def findSecondMin(arr):
	first = float('inf')
	second = float('inf')

	for i in arr:
		if i < first:
			second = first
			first = i
		if i > first and i < second:
			second = i
	return second
print(findSecondMin([3,6,2,8,5,1,0]))
