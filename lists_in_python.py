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

num_list = range(1, 11)
cubed_nums = []

# Normal way
for num in num_list:
    cubed_nums.append(num ** 3)

print(list(num_list))#> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cubed_nums) #>[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

print('----List comprehention------')

num_list = range(1, 11)
cubed_nums = []

cubed_nums = [num ** 3 for num in num_list]

print(list(num_list))#> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cubed_nums) #>[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

print('more--------another normal example, with a conditional ')

num_list = range(1, 11)

even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

print(list(num_list))#> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers) #>[2, 4, 6, 8, 10]

print('more--------another list comprehention example,with a conditional ')

num_list = range(1, 11)

even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))#> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers) #>[2, 4, 6, 8, 10]

print('----------')

#GLOBBING
one, two, three = [1, 2, 3]

print(one)#>1
print(two)#>2
print(three)#>3

one, *two, three = [1, 2, 3, 4, 5, 6]

print(one)#>1
print(two)#>[2, 3, 4, 5]
print(three)#>6

#REMOVE FIRST AND LAST ELEMENT


def remove_first_and_last(lists_to_clean):
    _, *content, _ = lists_to_clean
    return content

html = ['Removable', '<h1>', 'Some Content', '<h2>', 'Removable_too']

print(remove_first_and_last(html)) #> ['<h1>', 'Some Content', '<h2>']

print('-------Excercise on hold-------')
#It is useful to add error responses



html = ['Removable', '<h1>', 'Some Content', '<h2>', 'Removable_too']
html2= ['one', 'two']

def remove_first_and_last(lists_to_clean):

    if len(lists_to_clean) > 3:
            _, *content, _ = lists_to_clean
            return content
            print(remove_first_and_last(lists_to_clean))
    else:
        print('You need at least three elements for globbing')

print(remove_first_and_last(html2))