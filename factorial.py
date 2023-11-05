# Write a program for a factorial

# 1.find a factorail for a given number
# 2.find a factorail upto given number
# 3.find a factorial between ranger i.e; (start_range ,end_range)
# 4.Using built-ins (math module)

# using for loop
n=5 # input(input('Enter a number:'))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# using while loop

n=5 # int(input('Enter a number:'))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)


# using functions

def factorial(n):
    """
    Calculates the factorial of a given number.

    Args:
    n (int): The number for which the factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result


def factorial_upto_n(a):
    """
    Calculates factorials for numbers up to a given number.

    Args:
    a (int): The number up to which factorials are to be calculated.

    Returns:
    str: A formatted string showing the factorials for each number up to the given number.
    """
    fact_list = []
    for i in range(a):
        factorial_result = 1
        for j in range(1, i + 1):
            factorial_result *= j
        fact_list.append((i, factorial_result))
    return f'Factorials for numbers up to {a} are: {fact_list}'


def factorial_between_range(start, end):
    """
    Calculates factorials for numbers within a given range.

    Args:
    start (int): The starting value of the range.
    end (int): The ending value of the range.

    Returns:
    str: A formatted string showing the factorials for each number within the given range.
    """
    fact_list = []
    for i in range(start, end + 1):
        factorial_result = 1
        for j in range(1, i + 1):
            factorial_result *= j
        fact_list.append((i, factorial_result))
    return f'Factorials between {start} and {end} are: {fact_list}'


# Example usage of the functions
print(factorial(5))
print(factorial_upto_n(10))
print(factorial_between_range(4, 12))


import math
n=5
a=math.factorial(n)
print(a)

factorial_upto_givennuber=[math.factorial(i) for i in range(1,n+1)]
print(factorial_upto_givennuber)
x=5
y=12
factorial_between_range=[math.factorial(i) for i in range(x,y+1)]
print(factorial_between_range)