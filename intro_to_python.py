# string uses

sentence = 'the wick brown fox jumped over the lazy dog fence'

sentence_two = 'that is my dog\'s bowl'

sentence_three = "that is my dog's bowl"

sentence_four = "Tifany said, \"That is my dog's bowl\""

print(sentence_four)

sentence = 'the quick brown fox jumped'
sentence_two_upper= sentence.upper()

print(sentence)
print(sentence_two_upper)

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped'.title()
print(sentence)

sentence = 'THE QUICK BROWN FOX JUMPED'.lower()
print(sentence)

ZERO BASED NUMBERING SYSTEM - Acces a String
The qick brown fox jumped
T => 0
h => 1
e => 2
' ' => 3

starter_sentence = 'The quick brown fox jumped'
first= starter_sentence[0]
second = starter_sentence[1]
third = starter_sentence[2]
new_sentence = first + second + third
# print(starter_sentence[0])
# print(starter_sentence[12])
print(new_sentence[1])

starter_sentence = 'The quick brown fox jumped'
first_word = starter_sentence[0:2]
new_sentence = first_word
print(new_sentence)

starter_sentence = 'The quick brown fox jumped'
new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)

Heredoc ---

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.
Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.
Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()
print(content)

content = """
Nullam id dolor id git stanibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""
print(repr(content))

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'
print(long_string)

FIND METHOD

sentence = 'the quick brown fox jumped over the lazy dog'

# query = sentence.find('oops')
# # query_two = sentence.index('oops')
#
# print(query)
# # print(query_two)
query = 'fox' in sentence
query_two = 'oops' in sentence
print(query)
print(query_two)

# IMMUTABILITY Replace--
sentence = 'the quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence)

RANGES - Negative index
sentence = 'the quick brown fox jumped over the lazy dog'
print(sentence[-4:])

STRIP LSTRIP
url = '    https://google.com   '
print(url.strip())

url = 'https://google.com'
print(url.strip('https://'))

url = 'https://google.com'

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()
print(url)

PARTITION FUNCTION
heading = 'Python: An Introduction ,and Python: Advanced'
header, _, subheader = heading.partition(': ')

print(header)
print(_)
print(subheader)

SPLIT FUNCTION , BREACK STRINGS
tags = 'python,coding,programing,developement'
list_of_tags = tags.split(',')
print(list_of_tags)
list_of_tags = tags.split()
print(list_of_tags)

heading = 'Python: An Introduction'
heading_list = heading.split(': ')
print(heading_list)

API´s
api_data = '5'
greeting = 'hi there'

print(api_data.isalpha())
print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())
