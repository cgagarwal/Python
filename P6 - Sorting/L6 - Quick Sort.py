# Divide N Conquerer algo (Comparison based)

from random import randrange  # randrange element from random library use for choosing pivot randomly

def partition(arr,start,end):
	''' This function sorts the list in a way such that all elements
	less than or equal to pivot are in left side and greater than pivot on right side
	'''
	pivot_index = randrange(start,end)          # randomly choose pivot index
	pivot = arr[pivot_index]            # pivot 
	arr[pivot_index] , arr[end] = arr[end] , arr[pivot_index]   # swap the pivot and last element 
  
	m = start               # indexes for swapping
	for i in range(start,end):
		if arr[i] <= pivot:         # if any element less tha pivot found then it swaps
			arr[i] , arr[m] =  arr[m] , arr[i]
			m += 1
	arr[end] , arr[m] = arr[m] , arr[end]       # swap the pivot and first element greater than pivot
  
	return m              # pivot index by which list is subdivided in two sections

def quick_sort(arr,start,end):
	'''This sorts the list recusively by pivot partition method
	'''
	if start >= end:        # if arr has no element or single element then return
		return
	
	pivot_index = partition(arr,start,end)    # pivot partitioned list
	quick_sort(arr,start,pivot_index - 1)     # recusive call at left part
	quick_sort(arr,pivot_index+1,end)         # recursive call at right part

	return # arr is sorted

'''
TC  =  theta(nlogn) || O( n square )              SC = O(logn)
Inplace (YES)                                     Untable
'''
