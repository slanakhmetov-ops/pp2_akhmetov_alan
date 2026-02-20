numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  #1 Keep only even numbers

numbers = [10, 15, 20, 25, 30]
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20)  #2 Keep numbers greater than 20

numbers = [0, -1, 5, -3, 2]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  #3 Keep only positive numbers

numbers = [-5, -10, 0, 5, 10]
non_negatives = list(filter(lambda x: x >= 0, numbers))
print(non_negatives)  #4 Keep only non - negative numbers

