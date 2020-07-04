#for in loops -> IT WILL LOOP FOR ALL THE ELEMENTS
#while loops -> YOU HAVE TO TELL IT WHEN TO STOP

#FOR IN LOOP
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)
#it also works with tuples
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
    print(player)

print('---------')

players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis',
}

for position, player in players.items():
    print('Position', position)
    print('Player Name', player)
# """
# Position 2b
# Player Name Altuve
# Position 3b
# Player Name Bregman
# Position ss
# Player Name Correa
# Position dh
# Player Name Gattis
# """

print('----------')

# you can also loop over Strings, 

alphabet = 'abcdefghi'

for letter in alphabet:
    print(letter)
# """
# a
# b
# c
# d
# e
# f
# g
# h
# i
# """

print('---------')
#LOOPING OVER RANGES

for num in range(1, 11):
    print(num)
# """
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# """
print('---------')
#you can also add intervals

for num in range(1, 11, 2):
    print(num)
# """
# 1
# 3
# 5
# 7
# 9
# """

print('--------')

#CONTINUE AND BREAK

usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa'
]
#Continue
for username in usernames:
    if username == 'cersei':
        print(f'Sorry, {username} is not allowed')
        continue
    else:
        print(f'{username} is allowed')
# """
# jon is allowed
# tyrion is allowed
# theon is allowed
# Sorry, cersei is not allowed
# sansa is allowed
# """
print('-----------')
#BREAK
for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    print(username)
# """
# jon
# tyrion
# theon
# cersei was found at index 3
# """
print('--------')

#WHILE LOOPS - You HAVE to tell it when to stop with a sentinel value

nums = list(range(1, 101))

while len(nums) > 0:
    print(nums.pop())
# """
# 100
# 99
# 98
# 97
# 96
# 95
# 94
# 93
# 92
# 91
# 90
# 89
# 88
# 87
# 86
# 85
# 84
# 83
# 82
# 81
# 80
# 79
# 78
# 77
# 76
# 75
# 74
# 73
# 72
# 71
# 70
# 69
# 68
# 67
# 66
# 65
# 64
# 63
# 62
# 61
# 60
# 59
# 58
# 57
# 56
# 55
# 54
# 53
# 52
# 51
# 50
# 49
# 48
# 47
# 46
# 45
# 44
# 43
# 42
# 41
# 40
# 39
# 38
# 37
# 36
# 35
# 34
# 33
# 32
# 31
# 30
# 29
# 28
# 27
# 26
# 25
# 24
# 23
# 22
# 21
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# """

# def guessing_game():
#     while True:
#         print('What is your guess?')
#         guess = input()

#         if guess == '42':
#             print ('You correctly guessed it')
#             return False
#         else:
#             print(f'No, {guess} is not the answer, please try again\n')

# guessing_game()

#COMBINING LISTS

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']
#It wont work to only do the following

raw_database = [legacy_customers, new_customers]
print(raw_database)#>[['Alice', 'Bob'], ['Tiffany', 'Kristine']]
#becuse it prints them in their own list


for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers) #>['Tiffany', 'Kristine', 'Alice', 'Bob']







