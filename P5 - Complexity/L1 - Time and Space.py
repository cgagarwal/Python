# Time Complexity   ( 10..8 cycles per second )
'''
Best Case           [Big Omega notation]
Average Case        [Big theta notation]
Worst Case          [Big o notation]    O(n)
'''       # Base on Time

# Space Complexity    ( Base on Memory Use )
'''
Recursion Logic -->   Call of Stack
List / Arrays
Data sturcures  --->  Maps / Dict
Import modules have their own space complexity
'''

# Divide N conquerer based algorithms
'''       MASTER THEOREM
T(n) = a . T(n/b)  +  O (n..d   (logn)..p)
'''     # a >= 1  ,  b > 1  , d >= 0  , p = real no .. , .. means power

if log a base b < d :
  TC = O(n..d  (logn)..p)
elif log a base b = d :
  TC = O(n..d  (logn)..(p+1))   # log is multiplied
else:
  TC = O(n..( log a base b ))
  
'''  T(n)  =  T ( root n ) +  1 ''' # TC = O(loglogn)
