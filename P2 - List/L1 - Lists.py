# Lists are mutable i.e. updatable

li = [4,3,2,'hji',True,None,3.8]      # Heterogeneous
a = len(li)                           # length of list (7)

''' 0 to n-1  ||  -len(n) to -1 '''       # indexing

li[4] = 0         # updation


# Functions on list     [1,2,5]
c = li.copy()           # make a copy of list

li.append(12)          # append 12 at last      [1,2,5,12]
li.pop()              # remove last element     [1,2,5]
li.pop(2)             # 2 element removed       [1,2]
li.extend([1,6])        # append multiple       [1,2,1,6]
li.remove(1)          # first occurence of 1 removed    [2,1,6]
li.insert(1,8)        # 8 is inserted at 1 index        [2,8,1,6]
li.insert(57637,12)      # inserts at last              [2,8,1,6,12]
li.reverse()             # reverse the list          [12,6,1,8,2]
li.count(2)              # count occurrence of 2   (1)
li.sort()                # sorts the list (ascending)   [1,2,6,8,12]
li.clear()               # clears the list i.e. empty       []


print([1,2]+[2,3])          # Concatenation     [1,2,2,3]
print([1,5]*3)              # Replication     [1,5,1,5,1,5]
