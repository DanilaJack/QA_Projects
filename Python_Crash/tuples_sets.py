# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')

#Create a tuple with constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#needed comma in the end otherwise it's just a string
fruits3 = ('Apple',)

print(fruits, fruits2, fruits3)

#Get a value
print(fruits[1])

#Can't change the value
#fruits[0] = 'Pears'

#Delete tuple
del fruits2

#Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a set
fruits_set = {'Apples','Oranges', 'Mango'}


#Check is in a set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')
print(fruits_set)

#Remove from set
fruits_set.remove('Grape')

#Add duplicate
fruits_set.add('Apples')
print(fruits_set)


#Clear set
# fruits_set.clear()
# print(fruits_set)
#
# #Delete set
# del fruits_set

