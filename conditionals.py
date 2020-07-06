age = 126

if age < 25:
    print(f'I´m sorry you nedd to be at least 5 years old')
elif age > 100:
    print(f'I´m sorry {age} is too old to rent a car')
else:
    print(f'you are good to go, {age} fits in the age you can rent a car')


print('--------')
#TERNARY OPERATOR

role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)

print('--------')

role = 'admin'

if role == 'admin':
    auth = 'can acces'
else:
    auth = 'cannot access'

print(auth)

print('-----List of comparisonn opperators in comments------')

# == Equality
# != Inequality
# <> Inequality(deprecated operator DO NOT USE IT)
# > Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

print('----')

sentence = 'The quick brown fox jumped over the lazy Dog'

word = 'quick'

if word in sentence:
    print('the word was found in the sentence')
else:
    print('The word was not in the sentence')
#> the word was found in the sentence

sentence = 'The quick brown fox jumped over the lazy Dog'

word = 'dog'

if word in sentence:
    print('the word was found in the sentence')
else:
    print('The word was not in the sentence')
#>The word was not in the sentence

#It is cas sensitive so you can

sentence = 'The quick brown fox jumped over the lazy Dog'

word = 'dog'

if word.lower() in sentence.lower():
    print('the word was found in the sentence')
else:
    print('The word was not in the sentence')
#>the word was found in the sentence

print('-----')

nums = [ 1, 2, 3, 4]

if 3 in nums:
    print( 'the number was found')
else:
    print('the number was not found')

print('Compond conditionals---------')

#AND cotitional
username = 'Johanson'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'Johanson' and password == 'thenorth':
    print('acces permitted')
else:
    print('You shal not pass')
#acces permitted
print('------it is also possible---')

username = 'scar'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'Johanson':
    if password == 'thenorth':
        print('acces permitted')
else:
    print('You shal not pass')
#You shal not pass
print('----Or operator so if one r osme of the cotitional is true-------')

username = 'scar'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'Johanson' or password == 'thenorth':
    print('acces permitted')
else:
    print('You shal not pass')
#acces permitted

print('real world scenario -----------')

username = ''
email = 'jon@snow.com'
password = 'thenorth'

if (username == 'Johanson' or email == 'jon@snow.com') and password == 'thenorth':
    print('acces permitted')
else:
    print('You shal not pass')

print('--------')

logged_in = True 
standard_user = False

if logged_in and not standard_user:
    print('You can acces the admin dashboard')
else:
    print('You can only acces the standard dashboard')
