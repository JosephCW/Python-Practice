# 'regular' function
def func(a, b, c):
    print(a, b, c)


# function that provides some defaults
def func_defaults(a, b=2, c=3):
    print(a, b, c)


# function with a variable number of argumnets
def variable_func(*n):
    if n:
        for value in n[0:]:
            print('n:' + str(value))


# Variable keyword arguments
def kwargs_func(**kwargs):
    print(kwargs)


# Example using all previously used
def all_func(a, b, c=12, *args, **kwargs):
    print(a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


# Keyword based arguments
func(b=2, c=3, a=1)
# Function with default arguments
func_defaults(1)
func_defaults(1, c=3)
# Variable number of arguments
variable_func()
variable_func(1, 2, 3)
variable_func(-1, 2, 33, 12, 336)

# Variable unpacking
values = (1, 3, -7, 9)
# equivalent to: func((1, 3, -7, 9))
variable_func(values)
# equivalent to: func(1, 3, -7, 9)
variable_func(*values)

# Variable keyword arguments
# All calls equivalent. They print: {'a': 1, 'b': 42}
kwargs_func(a=1, b=42)
kwargs_func(**{'a': 1, 'b': 42})
kwargs_func(**dict(a=1, b=42))

#arguments must be given in the following order: positional arguments first (value), then any combination of keyword arguments (name=value), variable positional arguments (*name), then variable keyword arguments (**name).
all_func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
all_func(1, 2, 3, 5, 7, 9, A='a', B='b') # same as previous one

