# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Use a constructor
numbers2 = list((1, 2, 3, 4, 5))


#Get a value
print(fruits[1])

#Get a length of a list
print(len(fruits))

#append(add) to list
fruits.append('Mangos')
print(fruits)

#Remove from list
fruits.remove('Grapes')
print(fruits)

#Insert into position
fruits.insert(2, 'Strawberies')
print(fruits)

#Change value
fruits[0] = 'Blueberries'

#Remove with pop
fruits.pop(2)
print(fruits)

#Reverse list
fruits.reverse()
print(fruits)

#Sort list
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)

#Delete a list
del numbers

print(numbers2)