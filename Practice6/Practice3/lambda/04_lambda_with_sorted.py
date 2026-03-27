numbers = [5, 2, 9, 1, 5, 6]
ascending = sorted(numbers)
print(ascending)  #1 Sort numbers in ascending order

numbers = [5, 2, 9, 1, 5, 6]
descending = sorted(numbers, reverse=True)
print(descending)  #2 Sort numbers in descending order

words = ['apple', 'banana', 'cherry', 'date']
by_length = sorted(words, key=lambda x: len(x))
print(by_length)  #3 Sort words by length

words = ['apple', 'banana', 'cherry', 'date']
alphabetically = sorted(words, key=lambda x: x.lower())
print(alphabetically)  #4 Sort words alphabetically, case-insensitive
