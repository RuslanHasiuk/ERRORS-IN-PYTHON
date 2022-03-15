print('''
Type Errors
A TypeError is reported by the Python interpreter when an operation is applied to a variable of an inappropriate type.

This can occur in Python when one attempts to use an operator on something of the incorrect type.

For example, let’s see what happens when we try and add together two incompatible types:

piggy_bank = '2' + 0.25
There will be an TypeError error message:

Traceback (most recent call last):
  File "script.py", line 1, in <module>
    piggy_bank = '2' + 0.25
TypeError: must be str, not float
This error is reporting that 0.25 is not a string.

Some common type errors are:

Accidentally adding or subtracting a string value.
Call a function on something of the incorrect type.
''')