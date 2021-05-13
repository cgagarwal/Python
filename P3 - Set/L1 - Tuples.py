# Tuples are immutable
# class <tuple>

tup = (4,6,8,4)

a = tup[0]        # accessing

''' Catenatian and Replication are valid
  bcoz they give a new string   '''

''' if from any function multiple values return
  then return as a tuple  '''

a = (12)     # integer
a = (12,)     # tuple

a = len(tup)    # length of tuple (4)
tup.count(4)      # 2
tup.index(6)      # return the index of that value (1)
