meal_completed = True
total = 100
tip = total * 1/5
total = total + tip

receipt = "Your total is " + str(total)

print(tip)
print(receipt)

first = 'Springer'
second = 'Bregman'
third= 'Altuve'

print(first)

first = third

print(first)

"""
list - a collection of data ( any kind of data)
dictionary - a list in wich every item has a det of values assosiated to that item
tuple -collection of items but a little different than a list

"""
# LISTS 

User Database Query
Kristine
Tiffany
Jordan

users = ['Kristine', 'Tiffany', 'Jordan'] #a list

print(users) #['Kristine', 'Tiffany', 'Jordan']


users.insert(1, 'Anthony') #['Kristine', 'Anthony', 'Tiffany', 'Jordan']


print(users) 

users.append('Ian') #['Kristine', 'Anthony', 'Tiffany', 'Jordan', 'Ian']

print(users)

print(users[2]) #Tiffany

print([users[2]]) #['Tiffany']

users[4] = 'Brayden' #['Kristine', 'Anthony', 'Tiffany', 'Jordan', 'Brayden'] remeber that strings are inmmutable

print(users)

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users) #> ['Kristine', 'Tiffany', 'Jordan', 'Leann']

users.remove('Jordan')

print(users) #> ['Kristine', 'Tiffany', 'Leann']

popped_user = users.pop() 

print(popped_user) #> Leann
print(users) #> ['Kristine', 'Tiffany']

del users[0]
print(users) #> ['Tiffany']

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [ 1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list) #> [42, 10.3, 'Altuve', ['Kristine', 'Tiffany', 'Jordan', 'Leann']]

user_list = mixed_list.pop()

print(user_list) #> ['Kristine', 'Tiffany', 'Jordan', 'Leann']
print(mixed_list) #> [42, 10.3, 'Altuve']


#List Query in Python

tags = ['python', 'development', 'tutorials', 'code']

#how many elements are inside

numbers_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(numbers_of_tags)
print(last_item)
print(index_of_last_item)


tags = ['python', 'development', 'tutorials', 'code']

print(tags) #> ['python', 'development', 'tutorials', 'code']

tags.sort()

print(tags) #> ['code', 'development', 'python', 'tutorials']

tags.sort(reverse=True)

print(tags) #> ['tutorials', 'python', 'development', 'code']

totals = [234 , 1, 543, 2345]

totals.sort(reverse=True)

print(totals) #> [2345, 543, 234, 1]
