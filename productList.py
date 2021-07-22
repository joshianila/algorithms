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


#print(productList([1,2,3,6]))

def productList1(arr):
	leftarr = []
	rightarr = []
	prd = []
	left = right = 1
	print(arr)
	for i in arr:
		leftarr.append(left)
		left = left*i
	#print(leftarr)

	for j in range(len(arr)-1,-1,-1):
		rightarr.insert(0,right)
		right = right * arr[j]
	#print(rightarr)
	for i in range(len(arr)):
		prd.append(leftarr[i]*rightarr[i])
	print(prd)

productList1([1,2,3,6])