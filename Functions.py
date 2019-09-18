# need to define function before calling it
# provide two blank lines before and after function definition
""" This is multiple line comment
"""
from builtins import ValueError


def my_function():
    """ This is function comment section """
    print("Hello")


def my_function2():
    """ This is function comment section """
    print("Hello2")
    return 10


def my_function3(val):
    """ This is function comment section """
    print("Hello2 " + val)
    return 10


def my_function4(val):
    """ This is function comment section """
    try:
        # sum1 = 10/0
        print("Hello2 " + val)
    except ZeroDivisionError:
        print(ZeroDivisionError)
    return 10


def my_function5(val):
    pass
    # put pass if an empty function


def my_function6(val1, val2):
    print(val1 + " " + val2)


my_function()
print(my_function2())
print(my_function3("John"))
print(my_function4("John"))
print(my_function5("John"))
print(my_function6(val2="Smith", val1="John"))       # keyword arguments, put them in the last
# because above function does not return, it print None at the end,
# by default function return None
my_function6(val2="Smith", val1="John")
