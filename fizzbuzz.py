

       
# The code I wrote

for num in range(1, 101):
    output = ''
    if num % 3 == 0 and num % 5 == 0:
        output = 'FizzBuzz'
    elif num % 3 == 0:
        output = 'Fizz'
    elif num % 5 == 0:
        output = 'Buzz'
    else:
        output = num
    print(output)



# the code I wish I wrote
def fizzbuzz(variables, *args):
    for num in range(*args):
        output = ''
        for variable in variables:
            if num % variable==0:
                output+=variables[variable]
        if output =='':
            output = num
        print(output)

variables = {3:'Fizz',5:'Buzz'}
fizzbuzz(variables,101)
