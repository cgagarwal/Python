# Very Bad when range of elements is High (Counting Based)
'''   Make a dicrionary in which key represent element of list 
    and value represents its frequency and then remove one by one '''
''' But to make it stable we modify the rule '''

def counting_sort(arr):
    '''only positive enitites allowed
    make a new list of frequency of elements as index and then its
    prefix sum which gives position of elements in new list
    '''
    a = [0]*(max(arr)+1)        # make a new list of element as a index
    for i in arr:           # fill the frequencies in new list
        a[i] += 1
    for i in range(1,len(a)):      # calculate prefix sum
        a[i] += a[i-1]
    sorted_arr = [0]*len(arr)         # make new list of original size
    for i in reversed(range(0,len(arr))):     # start checking the position of element
        sorted_arr[a[arr[i]] - 1] = arr[i]      # fill the element at correct index
        a[arr[i]] -= 1            # reduce one index because it is filled
    return sorted_arr
  
# k = range of elements (max(arr))
'''
TC = O(n + k)                   SC = O(n + k)
Inplace (NO)                    Stable
         No Swaps and Comparisons
'''
