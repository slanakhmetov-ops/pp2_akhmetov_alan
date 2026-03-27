#1 Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(1, N+1):
        yield i ** 2
n = int(input("Enter a number N, to generate the squares of numbers up to it: "))
for i in square_generator(n):
    print(i)

#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(N):
    for i in range (N+1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number n, to print the even numbers between 0 and it: "))
result = list(even_generator(n))
print(*result, sep=", ")

#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisibility_generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number n to iterate the numbers, which are divisible by 3 and 4, between a given range from 0: "))
for i in divisibility_generator(n):
    print (i)            

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(A,B):
    for i in range (A, B+1):
        yield i*i
a, b = map(int, input("Enter numbers a and b to print the square of all numbers between them: ").split())        
for i in squares(a, b):
    print(i)

#5 Implement a generator that returns all numbers from (n) down to 0.
def downwards(N):
    for i in range (N, -1, -1):   
        yield i
n = int(input("Enter a number n to print all numbers from it down to 0: "))
for i in downwards(n):
    print(i)
