def full_name():
    print('hi')
#
#common convention to leave two lines after the function definition
full_name()

def full_name(first, last):
    print(f'{first}  {last}')


full_name('Kristine', 'Hudgens')
full_name('Elizabeth', 'Martinez')

print('-Authentication-----')

def auth(email, password):
    if email == 'j@johnangeles.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not Autorized')


auth('j@johnangeles.com', 'secret')
auth('j@johnangeles.com', 'error')

print('-with no arguments----------')

def hundred():
    for num in range(1, 11):
        print(num)


hundred()

def counter(max_value):
    for num in range(1, max_value):
        print(num)


counter(51)

print('printing or returning-----')
#Print, is for debugging, when werpint a value , it returns nothing
def full_name(first, last):
    print(f'{first}  {last}')


full_name('ELizabeth', 'Martinez')

print('---Return--------')
#Return, will return a value to another part of the program where is needed

def full_name(first, last):
    return f'{first}  {last}'


Eli = full_name('Elizabeth', 'Martinez')

def greeting(name):
    print(f'Hi {name} !')

greeting(Eli)
#>Hi Elizabeth  Martinez !

print('----Nested functions--------')
#Nested functions, if you are going to use a nested function in some other part of the program, then do not nest it

def greeting(first, last):
    def full_name():
        return f'{first}  {last}'

    print(f'Hi {full_name()} !')

greeting('Elizabeth', 'Martinez')

#>Hi Elizabeth  Martinez !

print('-------Default arguments----------')

def greeting(name = 'Guest'):
    print(f'Hi {name}!')


greeting() #>Hi Guest!
greeting('Elizabeth')#>Hi Elizabeth!

#The WRONG WAY IS THE FOLLOWING - do not us a mutable datatype as a default

def some_function(collection = []):
    collection.append(1)
    print(id(collection))
    return collection


print(some_function()) #> [1]
#If I call this somewhere else in the program

print(some_function()) #> [1, 1] because of the lists datatype mutability , the program went back to the fist time you used it and returned also the saved value from before

print('---------Name function arguments')
#if the are more than two arguments I´d use name arguments
def full_name(first, last):
    print(f'{first} {last} ')

#name arguments explicitly declare the mapping
full_name(last = 'Martinez', first = 'Elizabeth')#>Elizabeth Martinez

print('---------Unpacking------')
#*args represent a list of items that are going to be unpacked , that are going to be passed into the function
# common convention = *args => little for arguments
def greeting(*args ):
    print('Hi ' + ' '.join(args))


greeting('Elizabeth', 'Martinez') #> Hi Elizabeth Martinez
greeting('Elizabeth', 'Eleonor', 'Martinez', 'Arriaga') #> Hi Elizabeth Eleonor Martinez Arriaga 
#This is working with Tuples, so you canuse Tuples behavior
def greeting(*args ):
    print(args)


greeting('Elizabeth', 'Martinez') #>('Elizabeth', 'Martinez')
greeting('Elizabeth', 'Eleonor', 'Martinez', 'Arriaga') #>('Elizabeth', 'Eleonor', 'Martinez', 'Arriaga')
#you can also combine diferent kind of arguments
def greeting(time_of_day ,*args ):
    print(f"Hi {' '.join(args)} ,I hope that you are having a good {time_of_day}")


greeting('Morning', 'Elizabeth', 'Martinez') 
greeting('Afternoon', 'Elizabeth', 'Eleonor', 'Martinez', 'Arriaga')

print('--------Un packings Keyword Arguments--------')
#keyword arguments return a dictinary, 
# the common convention is(**kwargs)
def greeting(**kwargs ):
    print(kwargs)


greeting(first = 'Elizabeth', last = 'Martinez')
#> {'first': 'Elizabeth', 'last': 'Martinez'}
#now lets take a conditional
def greeting(**kwargs ):
      if kwargs:
          print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
      else:
          print('Hi Guest! have a great day')
#careful with the double string comillas

greeting(first = 'Elizabeth', last = 'Martinez')#>Hi Elizabeth Martinez, have a great day!
greeting()#>Hi Elizabeth Martinez, have a great day!

print('-------combine all argument types in a single function----')

def greeting(time_of_day, *args, **kwargs ):
    print(f"Hi {' '.join(args)}, I hope you are having a great {time_of_day}")

    if kwargs:
        print('Your tasks for the day are:')
        for key, val in kwargs.items():
            print(f"{key} => {val}")


greeting(
    'Morning',
    'Elizabeth','Martinez',
    first = 'Empty dishwasher',
    second = 'Take pupper outside',
    third = 'Math homework'
)
# Hi Elizabeth Martinez, I hope you are having a great Morning
# Your tasks for the day are:
# first => Empty dishwasher
# second => Take pupper outside
# third => Math homework

print('-----Lambdas----')

full_name = lambda first, last: f'{first} {last}'

full_name('Elizabeth', 'Martinez')

# You can treat it like a function, a lambda returns a value
#usually small behavior
full_name = lambda first, last: f'{first} {last}'

def greeting(name):
    print(f'Hi there {name}')


greeting(full_name('Johnattan', 'Angeles'))
#>Hi there Johnattan Angeles
