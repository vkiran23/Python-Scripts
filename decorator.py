# Decorators are Python functions that allow you to
# wrap another function as an input and modify its 
# behavior without altering the wrapped function’s code.
# They are used to extend the behavior of a particular object, 
# such as a class, method, or function. This approach promotes 
# reusability, modularity, and separation of concerns in your Python programs.


# Use cases for Decorators
# Decorators are widely used for a variety of purposes, such as:

# Timing function execution
# Caching results (memoization)
# Authorization and authentication
# Logging and error handling
# Input validation



# built-in decorators
# 1.property
# 2.staticmethod
# 2.classmethod
# 4.abstract method


# def outerfun(func):
#     def wrapper():
#         func()
#         func()
#     return wrapper

# @outerfun
# def twice():
#    print( 'Hello World!')

# twice()






import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        execution_time=end_time-start_time
        print(f'Execution time: {execution_time:.5f} seconds')
        return result
    return wrapper

@timer
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))

# @timer
# def simple_function(n):
#     for _ in range(n):
#         pass

# print(simple_function(10000))


