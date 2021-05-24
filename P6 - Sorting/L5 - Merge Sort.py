# Comparison based      (Divide and Conquerer Technique)
'''  T(n) = 2 T(n/2) + O(n)  '''

def merge(a,b):
    '''This function merges two sorted list 'a' and 'b' in sorted way
    '''
    n , m = len(a) , len(b)
    i , j = 0 , 0
    arr = []  # new liat is formed
    while i < n and j < m:
        if a[i] > b[j]:
            arr.append(b[j])
            j += 1
        else:
            arr.append(a[i])
            i += 1
    while i < n:
        arr.append(a[i])
        i += 1
    while j < m:
        arr.append(b[j])
        j += 1
    return arr

def merge_sort(arr,start,end):        # start = starting index ; end = last index
    '''this function makes recursive calls and at last single element
    remains which is always sorted and start merging all
    '''
    if start == end:              # if in array only one element left 
        return [arr[start]]       # gives that element as a element in list
    
    mid = (start + end) // 2            # calculate mid value

    left = merge_sort(arr,start,mid)        # divide the list from start to mid index
    right = merge_sort(arr,mid+1,end)       # dvivde from mid+1 to last index
    sorted_arr = merge(left,right)          # merge both the halfs
    return sorted_arr

'''
TC  =  O(nlogn)              SC = O(n) [O(n + logn)]
Inplace (NO)                 Stable
No Swaps                     Comparisons =  O(nlogn)
'''
