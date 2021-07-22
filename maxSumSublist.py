def maxSumSublist(arr):
	curr_max = arr[0]
	global_max = arr[0]

	for i in range(1,len(arr)):
		if curr_max < 0:
			curr_max = arr[i]
		else:
			curr_max += arr[i]
		if global_max < curr_max:
			global_max = curr_max
	return global_max
print(maxSumSublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))