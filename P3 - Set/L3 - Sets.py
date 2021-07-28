# Sets are immmutable
# class <set>
''' They are basically keys of dictionary '''
''' They are randomly arranged so no indexing '''

s = set()       # initializing
s = {1,2,4,'gr'}

s.add(12)       # add the element
s.remove('gr')    # delete the element
s.discard(56)    # work like remove --- does not give error for invalid element
s.pop()         # remove element randomly

# take input of set in single line by mapping
S = set(map(int , input().split()))
# also by usinf for loop
