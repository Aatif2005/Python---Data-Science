squares = [x**2 for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

numbers = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(numbers)

pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)