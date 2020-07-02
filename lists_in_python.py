tags = ['python', 'development', 'tutorials', 'code']

# in this case you replaced the last element so it´s not for adding elements
# tags[-1] = 'Programming'
# print(tags) #> ['python', 'development', 'tutorials', 'Programming']

# adding without brackets divides each character
# tags.extend('Programming')
# print(tags) #> ['python', 'development', 'tutorials', 'code', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']

#so this is the one way to add an elemnt to the end f the list BUTit does not store a new value, just like the sort function
tags.extend(['Programming']) #if you place this in a variable it will return = none
print(tags) #> ['python', 'development', 'tutorials', 'code', 'Programming']

tags = ['python', 'development', 'tutorials', 'code']

new_tags = tags + ['Programming']

print(new_tags) #>['python', 'development', 'tutorials', 'code', 'Programming']


