#Search a sorted array by dividing the search interval in half

# time complexity to O(1)
def binarySearch(array, left, right, x):
	while left <= right:
		mid = left + (right - left)//2
		#if the searched element is in the middle
		if (array[mid] == x):
			return mid;
		elif (array[mid] < x):
			left = mid+1 #ignore the left subarray
		else:
			right = mid -1 #ignore the right subarray

	return -1

#time complexity to O(Log n)
'''  
def binarySearch(array, left, right, x):
	if right>=left:
		mid = left + (right - left)//2
		#if the searched element is in the middle
		if (array[mid] == x):
			return mid;

		#the element is smaller than mid, then it can only be in the left subarray
		elif (array[mid]>x):
			return binarySearch(array, left, mid-1, x)

		#else the element can only be in the right subarray
		else: 
			return binarySearch(array, mid+1, right, x)
	else:
		return -1
'''

# Check the function
arr = [2,3,4,10,23,34,54,62,72,100]
x = 34

result = binarySearch(arr,0,len(arr)-1,x)

if result != -1:
	print ("Element is at index % d" %result)
else:
	print ("Element is not in array")
