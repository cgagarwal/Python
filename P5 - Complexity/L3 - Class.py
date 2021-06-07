# Object
''' everything in python is object with its properites
  and class is like an object constructor  '''

# Class         (Simplest form)
class Myclass:          # use keyword class
  x = 9
  
a = Myclass()         # a is an object
print(a.x)            # 9 

# __init__ function
''' This is a function in class which is always executed when class is initiated
use for asssigning values and for other necessary operations '''

class Person:
  def __init__(self , name , arg):  # self is not a keyword it is always first parameter
    self.name = name
    self.age = arg
  def fun(self):
    print("Hello " + self.name)

y = Person("Chirag" , 18)
print(y.name)             # Chirag
print(y.age)              # 18
y.fun()                   # Hello Chirag

''' Self is not neceesary u can call it whatever u want '''
y.age = 28          # modify object properties
del y.age           # age property is deleted
del y               # object deleted

class abc:
  pass        # pass for avoid error
print(abc)    # <class '__main__.abc'>
