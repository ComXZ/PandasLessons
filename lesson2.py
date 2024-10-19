import pandas

numbers = []
numbers_squares = []
for i in range(100):
    numbers.append(i)
    numbers_squares.append(i**2)

squares = pandas.Series(numbers_squares, numbers)
print(squares)

print(squares[-3:])
print(squares.tail(3))

print(squares[-3:].equals(squares.tail(3)))