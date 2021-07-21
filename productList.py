def productList(arr):
	left = 1
	prd = []	
	for i in arr:
		prd.append(left)
		left = left * i
	print(prd)

	right = 1
	for j in range(len(arr)-1,-1,-1):
		prd[j] = prd[j]*right
		right = right * arr[j]
	return prd


print(productList([1,2,3,6]))
