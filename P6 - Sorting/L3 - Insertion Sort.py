# sorts from first index  (Comparison Based)

def insertion_sort(arr):
	'''This sort finds the correct place of element and then
	insserts element there by one by on swapping
	'''
    for i in range(1,len(arr)):
        t = arr[i]      # we have to store the index because after swapping value at i index changes
        for j in reversed(range(0,i)): 
            if t < arr[j]:      # check the place in sorted region
                arr[j+1] , arr[j] = arr[j] , arr[j+1]   # swap when elements is lesser than another one
            else:
                break   # correct place finds
    return arr
  
'''
TC  =  O( n square )  ||  Omega (n)                   SC = O(1)
Inplace (YES)                                         Stable
Swaps  = O( n square )                                Comparisons =  O(n..2)    ||  Omega (n)
'''
