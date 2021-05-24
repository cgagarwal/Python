''' Modules are some libraries '''

import this       # Zen of Python

# Inbuilt Modules
import module_name

import math           # Math module
a = math.factorial(6)
a = math.log(123)

from math import *      # from math ; import all functions
a = log(23)
a = factorial(12)

from math import log10 , factorial      # import function
a = log10(1000)               # 3.0
a = math.floor(5.48)          # 5


# Array
x = array.array('type',list)    # i (int 2 byte) , f (float 4 byte) , d (double 8 byte)

import array as arr
x = arr.array('i', [1,2,3])

# help(module_name)

# OWN Module
''' MODULE IS IN SAME FOLDER
  import file_name
  file_name.function(arg)   '''
