#a lists uses []
# a dictionary uses {}
#a tuple uses ()

#TUPLE IS IMMUTABLE
#LIST IS MUTTABLE
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')
#the following is unpacking
title, sub_heading, content = post
#this is the same as querying the elemnts on a time
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

#LEVERAGING REASSIGNMENT it overrided it
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')
#it has to have the coma so it recognizes it aslso as a tuple
post = post + ('published',) #can also be writte as
post += ('Published',)


title, sub_heading, content, status , secon_status = post

print(post)#>('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')
print(title)#> Python Basics
print(sub_heading)#> Intro guide to Python
print(content)#> Some cool python content
print(status)#> published

# ID FUNCTION, to know what number is given in the memory to the variable
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')
 
print(id(post))
print(id(post))

post += ('published_three',)
#new object in memory
print(id(post))

#NESTED TUPLES
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['Python', 'Coding', 'Tutorial']

post += (tags,)

print(post) #> ('Python Basics', 'Intro guide to Python', 'Some cool python content', ['Python', 'Coding', 'Tutorial'])
print('----')
print(post[-1][1])#> Coding

#SLICE PYTHON TUPLES
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'more content', 'even more', 'last one', 'okay real last one')

print(post) #>('Python Basics', 'Intro guide to Python', 'Some cool python content', 'more content', 'even more', 'last one', 'okay real last one')
print(post[:2]) #>('Python Basics', 'Intro guide to Python')
print(post[1::2])#>('Intro guide to Python', 'more content', 'last one')

#REMOVE ELEMENTS FROM A TUPLE - remember because of tuple´s immutability it will not actually change the original tuple 
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'fourth', 'fifth', 'sixth', 'seventh')

#Removing elements from end
post = post[:-1] 
print(post)#>('Python Basics', 'Intro guide to Python', 'Some cool python content', 'fourth', 'fifth', 'sixth')

#Removing elements from beginning
post = post[1:] 
print(post)#>('Intro guide to Python', 'Some cool python content', 'fourth', 'fifth', 'sixth')

# #Removing specific element ( messy/ NOT RECOMMENDED)
post = list(post) 
print(post) #>['Intro guide to Python', 'Some cool python content', 'fourth', 'fifth', 'sixth']
post.remove('fourth')
print(post)#>['Intro guide to Python', 'Some cool python content', 'fifth', 'sixth']
post = tuple(post)
print(post)#>('Intro guide to Python', 'Some cool python content', 'fifth', 'sixth')
# #FOR THIS LAST METHOD IS IMMPORTANT TO TURN IT BACK INTO THE DATA STRUCTURE IT PREVIOUSLY HAD

# #TUPLES AS DICTIONARY KEYS
priority_index = {
    (1, 'premier') : ['1', '34', '12'],
    (1, 'mvp') : ['84', '22', '24'],
    (2, 'standard') : ['93', '81', '3'],
}

print(list(priority_index.keys())) #>[(1, 'premier'), (1, 'mvp'), (2, 'standard')]

#ZIP FUNCTION
positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)
print(scoreboard) #this returns a zip object so you hve to cast it into a list

scoreboard = zip(positions, players)
print(list(scoreboard)) #>[('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]

