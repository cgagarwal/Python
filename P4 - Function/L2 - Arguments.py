# Required Arguments
def fn(x,y,z):
  pass

fn(2,3,4)       # x = 2 , y = 3 , z = 4

# Keyword Arguments
fn(y = 2 , x = 4 , z = 7)

# Default Arguments
def fun(x, y = 11 , z = 12):
  pass

fun(12,15)        # x = 12 , y = 15 (updated) , z = 12 (default)
''' all default arguments are at rightermost side '''

# Variable length Arguments

def fun(*nums):
  pass

fun(10,112,33,2,31,2)     # for accessing , num is a tuple of variable

'''   A list in function is updated and changed globally
    but for string , int , bool , float copy of that is passed
    i.e. they remains same after executing function     '''

# Variable Length Keyword Arguments
def fnc(**args):
  print("Hello" + args['name'])
  
fnc(name = "Chirag")
