

       
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

#I like this one too from Jordan Hudgens

"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the
number and for the multiples of five print “Buzz”. For
numbers which are multiples of both three and five print
“FizzBuzz”.
"""

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)