# Python has functions for creating, reading, updating, and deleting files.

# Open a file (open - create the file)
MyFile = open('myfile.txt', 'w')

#Get some info
print('Name: ', MyFile.name)
print('Is Closed: ', MyFile.closed)
print('Opening Mode: ', MyFile.mode)

#Write to file
MyFile.write('I lovemy mum')
MyFile.write(' and papa')
MyFile.close()

#Append to file
MyFile = open('myfile.txt', 'a')
MyFile.write(' I also like my sister ')
MyFile.close()

#Read from a file
MyFile = open('myfile.txt', 'r+')
text = MyFile.read(100)
print(text)
