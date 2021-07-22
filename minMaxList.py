def minMaxList(arr):
	arr1 = []
	i = 0
	j = len(arr)-1

	while i<j:
		arr1.append(arr[j])
		arr1.append(arr[i])
		i += 1
		j -= 1
	arr1.append(arr[j])
	return arr1
print(minMaxList([1,2,3,4,5]))


def max_min1(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1
    print(lst)        
    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst
print(max_min1([1,2,3,4,5]))