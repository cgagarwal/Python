''' Inheritance allows a class to inherit all properties of another class
  Parent Class (base class)   --    Child Class (derived class) '''

class Person:     # any class can be parent class
  def __init__(self , name , arg):
    self.name = name
    self.age = arg
  def fun(self):
    print("Hello " + self.name)
    
class Student(Person):    # child class of Person
  pass

x = Student("Chirag", "21")
print(x.name)       # Chirag
print(x.age)        # 21

class Student(Person):      # child class inherit function overrides the inherit function of Parent Class
  def __init__(self,name,age):    # so Parent Class inherit function not inherits
    Person.__init__(self,name,age)    # call parent class inherit function for inheriting it

# for inheriting also use super() function
class Student(Person):
  def __init__(self,name,age):
    super().__init__(name,age)      # not need to use class name for inheriting
  def cool(self):
    print("Welcome" + ' ' + self.name)
 
x = Student("Chirag", "21")
x.cool()        # Welcome Chirag
