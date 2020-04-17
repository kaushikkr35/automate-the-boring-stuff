def spam(divide_by):
    return 42 / divide_by
try:
    print(spam(2))
    print(spam(10))
    print(spam(0))
except ZeroDivisionError:
    print('Error: You tried to divide by zero.')
