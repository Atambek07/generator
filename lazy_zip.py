"""
This function takes two generators and returns a generator that yields tuples
containing elements from both generators. It stops when either generator is exhausted.
"""

def lazy_zip(gen1, gen2):
    while True:
        try:
            x = next(gen1)
            y = next(gen2)
            yield (x, y)
        except StopIteration:
            return  

def count_from(n):
    while True:
        yield n
        n += 1

def letters():
    for c in 'abcdef':
        yield c

gen1 = count_from(1)
gen2 = letters()

lz = lazy_zip(gen1, gen2)

for pair in lz:
    print(pair)
