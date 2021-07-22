def rotateElements(arr,k):
	j = 0
	while j<k:
		last = arr[-1]
		for i in range(len(arr)-1):
			current = arr[i+1]
			arr[i+1] = arr[0]
			arr[0] = current
		arr[0] = last
		j += 1
	return arr
print(rotateElements([10,20,30,40,50],3))

def right_rotate(lst, k): 
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], abs(3)))

def right_rotate(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))