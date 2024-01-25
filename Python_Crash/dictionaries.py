# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#Create a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))

# #creation with use a constructor
# person2 = dict(first_name = 'Sara', last_name = 'Williams')
# print(person2, type(person2))

#Get a value
print(person['first_name'])
print(person.get('last_name'))

#Add key/value
person['phone'] = '555-55-5555'

#Get dict keys
print(person.keys())

#Get dict items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)


#remove item
del(person['age'])
person.pop('phone')
print(person)

#clear
person.clear()
print(person)

#Get length
print(len(person2))

# List of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[1]['name'])

