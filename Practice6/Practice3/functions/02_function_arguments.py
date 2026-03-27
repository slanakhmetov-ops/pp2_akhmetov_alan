def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") #1 A function with one argument

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument (#2 The terms parameter and argument can be used for the same thing: information that are passed into a function.)


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #3 This function expects 2 arguments, and gets 2 arguments


def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus") #4 You can assign default values to parameters. If the function is called without an argument, it uses the default value
