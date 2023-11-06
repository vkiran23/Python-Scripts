# Generators are functions that use the yield keyword to produce a sequence of values.
# They are particularly useful when dealing with large datasets or when you want to 
# iterate over a sequence without storing the entire sequence in memory at once.


def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib_ser=fibonacci_generator()

for i in range(10):
    print(next(fib_ser))


def generate_number(n):
    a=(x for x in range(n))
    return a

gen=generate_number(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
