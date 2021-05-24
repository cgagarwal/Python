# sorts from last index   (Comparison Based)

def bubble_sort(arr):
    '''this starts from first index and start comparing and swaps
    the element if first one is bigger and goes till last place
    '''
    for i in reversed(range(0,len(arr))):
        swapped = False  # swapped is initializing to reduce the comparisons in sorted list
        for j in range(0,i):
            if arr[j] > arr[j+1]: # check j and j+1 index
                arr[j] , arr[j+1]  = arr[j+1] , arr[j]
                swapped = True
        if not swapped: # if no swapping takes place that means arr is sorted
            return arr
    return arr
  
'''
TC  =  O( n square )  ||  Omega (n)                   SC = O(1)
Inplace (YES)                                         Stable
Swaps  = O( n square )                                Comparisons =  O(n..2)    ||  Omega (n)
'''
