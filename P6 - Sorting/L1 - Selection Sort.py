# sorts from first index  (Comparison Based)

def min_fn(arr, t):
    '''This fuction finds the min element's index in 'arr' starting from
    't' index.
    '''
    lst = t   # assume 't' to be min element index
    for i in range(t+1 , len(arr)): #iterate one by one in 'arr'
        if arr[i] < arr[lst]: # if element less than 't' found
            lst = i    # update the min element index
    return lst

def selection_sort(arr):
    '''this finds the min element in the list and swap the
    first element and min element with each other
    '''
    for i in range(0,len(arr)):
        j = min_fn(arr,i)
        if i != j:              # Swap the min element at its place
            arr[i] , arr[j] = arr[j] , arr[i]
    return arr
  
'''
TC  =  O( n square )          SC = O(1)
Inplace (YES)                 Unstable
Swaps  = O(n)                 Comparisons =  O(n..2)
'''
