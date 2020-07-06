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
#Print, is for debugging
def full_name(first, last):
    print(f'{first}  {last}')


full_name('ELizabeth', 'Martinez')

print('-----------')
#Return, will return a value to another part of the program where is needed

def full_name(first, last):
    return f'{first}  {last}'


full_name('Elizabeth', 'Martinez')

def greeting(name):
    print(f'Hi  {name}!')


greeting(Johnattan)