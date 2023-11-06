# In Python, an iterator is an object that allows you to traverse a container, 
# such as a list, tuple, or dictionary. It provides a way to access the elements
# of a container one at a time without needing to know the underlying structure of the container. 
# Iterators are used in conjunction with the iter() and next() functions.

# An iterator in Python must implement two methods:

# __iter__: Returns the iterator object itself. 
# This allows the iterator to be used in a for loop.


# __next__: Returns the next item in the container. 
# If there are no more items, it raises the StopIteration exception.

my_list = [1, 2, 3, 4, 5]

my_iter=iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))