numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) #1 Double all numbers in a list


numbers = [10, 20, 30, 40]
str_numbers = list(map(lambda x: str(x), numbers)) 
print(str_numbers) #2 Convert all numbers to strings


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))  
print(squared) #3 Square all numbers in a list


numbers = [5, 10, 15, 20]
halved = list(map(lambda x: x / 2, numbers))  
print(halved) #4 Halve all numbers in a list

