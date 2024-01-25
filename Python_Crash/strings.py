# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + 'and I am ' + str(age))


# String Formatting

#Arguments by position
print ('My name is {name} and I am {age}'.format(name=name, age=age))

#F-strings
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

#Capitalize string
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lowercase
print(s.upper().lower())

#Swap case
print(s.capitalize().swapcase())

#Get length
print(len(s))

#Replace
print(s.replace('world', 'everyone'))

#Count
sub = 'l'
print(s.count(sub))

#Starts with
print(s.startswith('ello'))

#Ends with
print(s.endswith('d'))

#Split into a list
print(s.split())

#Find position
print(s.find('o'))

#Is all alphanumeric
print('hellow68orld'.isalnum())

#Is all alphabetic
print('helloworld'.isalpha())

#Is all numeric
print('645789'.isnumeric())

