# HW6 Mathmatical Series


def fibonacci(n):
    """Defining a function  called fibonacci to provide nth value in fibonacci
    sequence."""
    if n == 0:
        return 0
    # First value in fibonacci sequence is 0.
    elif n == 1:
        return 1
    # Second value in fibonacci sequence is 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    """Formula for fibonacci sequence after first two values.  Function calls
    itself and sums the values to provide the nth value starting from 0."""


def fib(n):
    """Function to print fibonacci function"""
    print (fibonacci(n))


fib(3)  # test to see if fibonacci function is printing correct value
fib(5)  # test to see if fibonacci function is printing correct value


def lucas(n):
    """New function called lucas to provide nth value in lucas numbers."""
    if n == 0:
        return 2
    # Setting the first value to match that of the value in Lucas numbers.
    elif n == 1:
        return 1
    # Setting the second value to match that of the value in Lucas numbers.
    else:
        return lucas(n-1) + lucas(n-2)
    """Formula for Lucas numbers after first two values. Function calls itself and
    sums the values to provide the nth value starting from 0."""


def luc(n):
    """Function to print lucas function."""
    print (lucas(n))


luc(0)  # testing lucas function is printing correct values
luc(1)  # testing lucas function is printing correct values
luc(2)  # testing lucas function is printing correct values
luc(3)  # testing lucas function is printing correct values
luc(4)  # testing lucas function is printing correct values


def sum_series(x, y=0, z=1):
    """Function that provides nth value in either the fibonacci sequence or
    lucas numbers. First argument is required to get nth value and y and z
    are optional."""
    if y == 0 and z == 1:
        return fibonacci(x)
    # If only one argument is provided in function, defaults to providing
    # fibonacci nth value.
    elif y == 2 and z == 1:
        return lucas(x)
    """If argument is provided with parameters matching lucas numbers,
    the nth value in lucas numbers is given."""


def sum_s(n, y=0, z=1):
    print(sum_series(n, y, z))
    """function to print sum_series function"""

sum_s(5)  # test to see if sum_series function is calling fibonacci
sum_s(5, 2, 1)  # test to see if sum_series is calling lucas numbers


if __name__ == "__main__":
    assert fibonacci(5) == 5  # tests 5th value of fibonacci sequence
    assert lucas(3) == 4  # tests 3rd value in lucas number to match sequence
    assert sum_series(0) == 0  # test function if it defaults to fibonacci
    assert sum_series(0, 2, 1) == 2  # test to see if it calls lucas function