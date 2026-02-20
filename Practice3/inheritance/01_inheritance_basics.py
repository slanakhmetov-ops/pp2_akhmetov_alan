class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() #1 Create a class named Person, with firstname and lastname properties, and a printname method


class Student(Person):
  pass #2 Create a class named Student, which will inherit the properties and methods from the Person class, Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("Mike", "Olsen")
x.printname() #3 Use the Student class to create an object, and then execute the printname method:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) #4 To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    


