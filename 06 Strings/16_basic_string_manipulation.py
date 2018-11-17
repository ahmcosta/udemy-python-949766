# There is no diference between single quote (') and double quote (")
# https://www.tutorialspoint.com/What-is-the-difference-between-single-and-double-quotes-in-python
string = 'I am a string in Python'
string1 = "I am a string in Python" 

print(len(string))

print(string[0]) # I
print(string[2]) # a
print(string[-1]) # n  => reverse index

print(string[7:13]) # string
print(string[7:])  # a string in Python
print(string[:4])  # I am

# string[-1] = 'x' # It won't work! 'str' object does not support item assignment

string2 = 'Con' + 'catenation' # Concatenation
print(string2)

string3 = 2 * 'Con' + 'catenation' # ConConcatenation
print(string3)

string4 = 2 * ('Con' + 'catenation')  # ConcatenationConcatenation
print(string4)

string5 = 'Con' 'catenation' # Concatenation wichout +
print(string5)

con = 'Con'
cat = 'catenate'
# print(con cat) # It won't work! Concatenation without + is only applyable for strings, not for variables

word = "Word"
word = 'L' + word[1:]
print(word) # Lord
