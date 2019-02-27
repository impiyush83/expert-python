# DECORATORS WITH ARGUMENTS :


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say("piyush", "nalawade"))

"""This makes debugging and working with the Python interpreter awkward and challenging. Thankfully there’s a quick 
fix for this: the functools.wraps decorator included in Python’s standard library. You can use functools.wraps in 
your own decorators to copy over the lost metadata from the undecorated function to the decorator closure. 


"""

import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()

    return wrapper


def italics(func):
    @functools.wraps(func)
    def wrapper():
        print(func())
        return "<i>" + func().lower() + "</i>"

    return wrapper


@italics
@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'

print(greet())

"""
Python Decorators – Key Takeaways * Decorators define reusable building blocks you can apply to a callable to modify 
its behavior without permanently modifying the callable itself. * The @ syntax is just a shorthand for calling the 
decorator on an input function. Multiple decorators on a single function are applied bottom to top (decorator 
stacking). * As a debugging best practice, use the functools.wraps helper in your own decorators to carry over 
metadata from the undecorated callable to the decorated one. 
"""
