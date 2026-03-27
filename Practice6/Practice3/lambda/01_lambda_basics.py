x = lambda a : a + 10
print(x(5)) #1 Add 10 to argument a, and return the result

x = lambda a, b : a * b
print(x(5, 6)) #2 Multiply argument a with argument b and return the result 


x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #3 Summarize argument a, b, and c and return the result

def myfunc(n):
  return lambda a : a * n #4 Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number


