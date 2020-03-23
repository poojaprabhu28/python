print("This file has definitions of all basic Python operations")

#printing a statement/variable
name = input('What is your name? ')
print("Hello " + name)

#print the type of datatypes
print(type(2+4))
print(type(2 / 4))
print(type("hi hello there"))

#to the power
print(2 ** 3)

#prints rounded off and absolute values respectively
print(round(3.2))
print(abs(-4))

#binary numbers
print(bin(5))

#assigning constants
PI = 3.14

#augmented assignment operator
some_value = 5
some_value += 2
print(some_value)

#String excercises
#to print long strings with multiple lines
long_string = '''
My name is Pooja
I love noodles
I willbe the best programmer
'''
print(long_string)

#simple string concatenation
first_name = "Pooja"
last_name = "Prabhu"
full_name = first_name + ' ' + last_name
print(full_name)

#type conversion
a = 100
b = str(a)
c = int(b)
d = type(c)
print(d)

#escape sequence for \', \". \t, \n
weather = 'It\'s sunny'
print(weather)

#formatted strings
name = "Pooja"
age = 55
#in python 3
print(f'hi {name}. You are {age} years old')
#in python 2. not recommended
print('Hi {0}. Your age is {1}'.format('Pooja','55'))

#string indexeselfish = 'me me me'
selfish = '01234567'
print(selfish[0])
#[start:stop]
print(selfish[0:4])
#[start:stop:stepover]  #string slicing
print(selfish[0:8:2])
print(selfish[-1])

#String immutablity- a string index value cnnot be changed without reassigning the whole string

#built-in funtions are always available and are linked to the interpretor
greet = 'helloooo'
print(greet[0:9:1])

#methods are similar to functions- except that they belong to something, usually a class
print(greet.upper())
print(greet.capitalize())
print(greet.find('lo'))
print(greet.replace('lo','u'))

#Booleans
name = 'Pooja'
is_cool = False
is_cool = True
print(bool(0))
print(bool('True'))

#Excercise to caluculate age based on birth year
birth_year = input("what year were you born? ")
current_year = 2020
age = current_year - int(birth_year)
print(f"your age is {age}")


print(selfish[8])
