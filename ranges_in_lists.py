# tags = ['Python', 'development', 'tutorials', 'code', 'Another']
# tags_range = tags[1:3]

# print(tags_range) #> ['development', 'tutorials']

# tags = ['Python', 'development', 'tutorials', 'code', 'Another']
# tags_range = tags[1:]

# print(tags_range) #> ['development', 'tutorials', 'code', 'Another']


# tags = ['Python', 'development', 'tutorials', 'code', 'Another']
# tags_range = tags[:3]

# print(tags_range) #> ['Python', 'development', 'tutorials']

# tags = ['Python', 'development', 'tutorials', 'code', 'Another']
# tags_range = tags[:-1]

# print(tags_range) #> ['Python', 'development', 'tutorials', 'code']

# tags = ['Python', 'development', 'tutorials', 'code', 'Another']
# tags_range = tags[:]

# print(tags_range) #> ['Python', 'development', 'tutorials', 'code', 'Another']

# print('ADVANCE RANGES __________________')

# tags = [
#     'Python',
#     'development', 
#     'tutorials', 
#     'code', 
#     'Programming',
#     'Computer Science'
#     ]
# tags_range = tags[1:-1]

# print(tags_range) #> ['development', 'tutorials', 'code', 'Programming']

# tags = [
#     'Python',
#     'development', 
#     'tutorials', 
#     'code', 
#     'Programming',
#     'Computer Science'
#     ]
# tags_range = tags[:-1:2] #every other element

# print(tags_range) #>['Python', 'tutorials', 'Programming']

# tags = [
#     'Python',
#     'development', 
#     'tutorials', 
#     'code', 
#     'Programming',
#     'Computer Science'
#     ]
# tags_range = tags[::-1] #reverse th order of the index

# print(tags_range) #> ['Computer Science', 'Programming', 'code', 'tutorials', 'development', 'Python']

# tags = [
#     'Python',
#     'development', 
#     'tutorials', 
#     'code', 
#     'Programming',
#     'Computer Science'
#     ]
# tags_range = tags[::-1]

# print(tags_range)

# tags.sort(reverse=True) # sort does not return a value because of python´s immutability

# print(tags)

# sale_prices = [
#     100,
#     83,
#     220,
#     40,
#     100,
#     400,
#     10,
#     1,
#     3
# ]
# sorted_list = sale_prices.sort()

# print(sorted_list)

# sale_prices = [
#     100,
#     83,
#     220,
#     40,
#     100,
#     400,
#     10,
#     1,
#     3
# ]
# sorted_list = sorted(sale_prices, reverse=True)

# print(sorted_list)#>[400, 220, 100, 100, 83, 40, 10, 3, 1]
# print(sale_prices)#remains without changes [100, 83, 220, 40, 100, 400, 10, 1, 3]

print('---------------SLICE CLASS')

tags = [
    'Python',
    'development', 
    'tutorials', 
    'code', 
    'Programming',
    'Computer Science'
    ]
# tags_range = tags[:2]

print(tags[1:4:2])#> ['development', 'code']

slice_obj = slice(2)

print(slice_obj) #> slice(None, 2, None)

slice_obj = slice(1, 4, 2)

print(tags[slice_obj]) #> ['Python', 'development']

print(slice_obj.start) #> 1
print(slice_obj.stop)#> 4
print(slice_obj.step)#> 2

