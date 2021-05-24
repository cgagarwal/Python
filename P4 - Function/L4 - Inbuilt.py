from random import randrange
a = randrange(start,end)    # takes random value from start to end

print(abs(-4))                  # 4   absolute value
print(isinstance(10 , int))      # True 

import sys
a = sys.maxsize                         # max element in python
x , y = float('inf') , - float('inf')     # infinity

print("%0.6f"%num)              # value after 6 precedding digit of decimal

li = list(map(int , input().split()))     # for multiple input through mapping

from itertools import product         # Cartesian product
arr = [1,2]
print(list(product(arr,arr)))           # [(1, 1), (1, 2), (2, 1), (2, 2)]
print(list(product(arr,repeat = 3)))

A = [[1,2],[1,2,3]]
print(list(product(*A)))        #  [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]
