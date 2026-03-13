from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map
squares = list(map(lambda x: x**2, numbers))
print(squares)

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# reduce
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)