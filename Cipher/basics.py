#Variable is a name that references or points to an object
#variable_name = value

number = 5
text='Hello World'

#Functions are reusable code blocks that we can call, or invoke, to run their code when we need them
#To call a function: name the function with a pair of parenthesis
print(text)

#An argument is an object or an expression passed to a function - added between the opening and closing parenthesis

#Each string character can be referenced by a numerical index. Each character of a string can be referenced by using bracket notation
print(text[8])

#We can also assess the string from the end of the string. 
# Last char --> -1
# Second last char --> -2
print(text[-1])

# len() function gives the number of chars in a string
print(len(text))

#type returns the data type of the variable
print(type(text))

# Variable rules: can't start with a number, they can contain alphanumeric characters or underscores
# snake case is common in python

# A method is similar to a function but belongs to an object
# We'll use the find() method to find the position in the alphabet of each letter in our message
# Returns -1 if it can't find that character(or that char in lowercase)
print(text.find('H'))
print(text.find('h'.upper()))

