def rearrange(arr):
	i = 0
	j = len(arr)-1

	while i <= j:
		if arr[i] < 0:
			i += 1
		if arr[i] > 0:
			arr[i],arr[j] = arr[j],arr[i]
			j -= 1
	return arr
print(rearrange([-2,4,7,-9,5]))