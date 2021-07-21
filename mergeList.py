def mergeList(arr1,arr2):
	i = j = 0
	arr3 = []
	while i<len(arr1) and j<len(arr2):
		if arr1[i] <= arr2[j]:
			arr3.append(arr1[i])
			i += 1
		else:
			arr3.append(arr2[j])
			j += 1
	while j < len(arr2):
		arr3.append(arr2[j])
		j += 1
	while i < len(arr1):
		arr3.append(arr1[i])
		i += 1
	return arr3
print(mergeList([1,3,5],[2,4,6]))

def merge_arrays(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1


print(merge_arrays([4, 5, 6], [-2, -1, 0, 7]))