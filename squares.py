# This code defines a generator function that yields squares of numbers starting from a given number.
# The generator function `squares` takes an optional argument `start` which defaults to 1.
# It initializes a variable `n` to the value of `start` and enters an infinite loop.
# Inside the loop, it yields the square of `n` (i.e., `n * n`) and then increments `n` by 1.
# The generator can be used to generate squares of numbers indefinitely, starting from the specified number.
# The code then creates a generator object `sq` by calling the `squares` function with an argument of 3.    

def squares(start=1):
    n = start
    while True:
        yield n * n
        n += 1

sq = squares(3)
for _ in range(5):
    print(next(sq), end=' ')
print()
    