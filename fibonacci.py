"""Fibonacci sequence generator using a generator function in Python.
This code defines a generator function that yields Fibonacci numbers indefinitely."""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=' ')
print()

