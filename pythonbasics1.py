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

#password checker
user_name = input('Enter your user name: ')
password = input('Enter your password: ')
hidden_password = '*' * len(password)
print(f'Hi {user_name}, your password {hidden_password} is {len(password)} letters long')

#list initializing
amazon_cart = ['notebooks', 
'sunglasses',
'toys',
'grapes'
]
print(amazon_cart)
#list slicing
print(amazon_cart[0:2])
#list append
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
print(new_cart)
#new_cart = amazon_cart doesn't create a copy of amazon_cart. instead refers to the same list
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#matrix
matrixtest = [
  [1,0,2],
  [2,4,6],
  [3,6,9]
]
print(matrixtest[0][2])

#operations on lists
#functions
basket = [1,2,3,4,5]
print(len(basket))

#methods
basket.append(100)
print(basket)
basket.insert(4,150)
print(basket)
basket.extend([200])
print(basket)

#removing
basket.pop()  #pops the end of the list
print(basket)
basket.pop(0) #removes the object at index 0
print(basket)

new_list = basket.pop(2)
print(new_list)   #element at index 2
basket.clear()
print(basket)   #clears contents of basket

basket = ['a','b','c','d','e','d']
#print(basket.index('c',0,2))    #gives value error 'c' is not in list
print(basket.index('c',0,3))    #check availability in list within given range
print('d' in basket)
print('x' in basket)    #returns false as x is not in basket
print('i' in 'Hi my name is Ian')
print(basket.count('d'))    #gives count of number of times a value is repeated

basket = ['b','x','c','d','e','d','a']

basket.sort()
print(basket)
#print(sorted(basket))     #creates a new list of sorted basket. original basket remains unchanged as below
#print(basket)

#new_basket = basket.copy()
#print("new_basket")
#print(new_basket)

basket.reverse()
print(basket)

basket.sort()
basket.reverse()
#print(basket[::-1])   #new list
#print(basket)   #original basket

#print(list(range(1,100)))
#print(list(range(100)))    3starts from 0

sentence = ' '
new_sentence = sentence.join(['hi','my','name','is','Pooja'])   #join uses the string/item in sentence to join the list input and form the new string new_sentence
print(new_sentence)

#list unpacking 

a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

#None is a special datatype in python. Similar to null
#example in a game for a new user
wepons = None
print(wepons)

#dictionary has unordered key-value pairs (not adjecent in position in memory)
#key is a string used to access its adjoining value
#dictionary holds more value than, say, list
dictionary = {
  'a' : [1,2,3],
  'b' : "Hello",
  'x' : True
}

my_list = [
  {
    'a' : [1,2,3],
  'b' : "Hello",
  'x' : True
  },
  {
    'a' : [4,5,6],
  'b' : "Hello",
  'x' : True
  }
]

print(my_list[0]['a'][2])
print(dictionary['a'][0])

#a key needs to be immutable i.e it cannot change
#a key needs to be unique
dictionary = {
  '123' : [1,2,3],
  '123' : "Hello",    #value of '123' is overrriden
  True : "Hello",
  [100] : True    #gives error- TypeError: unhashable type: 'list
}

#Dictionary methods
user = {
  'basket' : [1,2,3],
  'greet' : "Hello"
}

user2 = dict(name='Pooja')    #creates a dictionary entry dict(key=vlue)

print(user2)
#print(user.get('age'))      #check's if a key exists in the dict
#print(user.get('age', 55))

user = {
  'basket' : [1,2,3],
  'greet' : "Hello",
  'age' :20
}

print('age' in user.keys())   #checks for a key's existance
print('Hello' in user.values())   #checks for a value's existance
print(user.items())   #gives key value pairs as tuples

user = {
  'basket' : [1,2,3],
  'greet' : "Hello",
  'age' :20
}

#user2 = user.copy()   #copies a dicctionary
#user.clear()          #clears a dictioanries of its values
#user2.pop('age')      #removes

#print(user)   
#print(user2)
#print(user2.pop('age'))      #removes/ returns some pair of key- value
print(user.update({'age':55}))    #updates an existing key's value
print(user)

#Tuples
