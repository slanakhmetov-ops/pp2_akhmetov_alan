def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message) #1 A function that returns a value


def get_greeting():
  return "Hello from a function"

print(get_greeting()) #2 Using the return value directly


def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) #3 A function that returns a list


def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y) #4 A function that returns a tuple