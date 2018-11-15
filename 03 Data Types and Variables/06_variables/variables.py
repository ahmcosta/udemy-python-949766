number = 2
real = 2.2
word = "word"
print(word)
print(type(word)) # <class 'str'>

# Multiple assingments for a same value
a = b = c = 1.5
print(a)
print(b)
print(c)

# Multiple assingments for multiple values
one, two, three = 1, 'two', 3.0
print(one)
print(two)
print(three)

# Python is a dynamically-typed language. 
# Java is a statically-typed language. 
# In a weakly typed language, variables can be implicitly coerced to unrelated types, whereas in a strongly typed language they 
# cannot, and an explicit conversion is required. 
# ... Both Java and Python are strongly typed languages
# More info in https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/

number = 1
str = 'string'
number = str

print(number)

# keywords list. They cannot be used for variable names
# ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword
print(keyword.kwlist)