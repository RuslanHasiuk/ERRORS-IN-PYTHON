print('''When we are writing Python programs, the interpreter is our first line of defense against errors.

SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong,
a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

Here’s an example of a SyntaxError error message:

File "script.py", line 1
  print(Hello world!)
                  ^
SyntaxError: invalid syntax
The interpreter will tell us where (the file name and line number) it got into trouble and its best guess as to what is wrong.

After reading the error message, we can assume that the cause for this error is a lack of quotation marks around Hello world!.

Some common syntax errors are:
- Misspelling a Python keyword.
- Missing colon :.
- Missing closing parenthesis ), square bracket ], or curly brace }.''')
