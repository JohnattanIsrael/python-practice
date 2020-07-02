# tags = {
#     'python',
#     'coding',
#     'tutorial',
# }
# print(tags)#this is the set data structure>{'tutorial', 'coding', 'python'}
# #a set is used when we don´t want to allow duplicates
# tags = {
#     'python',
#     'CODING',
#     'tutorial',
#     'CODING'
# }
# print(tags)#>{'python', 'tutorial', 'CODING'}

# #SET DOES NOT SUPPORT INDEXING
# #nope print(tags[0])

# query_one = 'python' in tags
# query_two = 'ruby' in tags

# print(query_one) #>True
# print(query_two) #>False

#MERGING PYTHON SETS

tags_one = {
    'python',
    'CODING',
    'tutorial',
    'CODING'
}

tags_two = {
    'ruby',
    'CODING',
    'tutorial',
    'development'
}

#merge tags
merged_tags = tags_one | tags_two
print(merged_tags) #>{'python', 'ruby', 'development', 'CODING', 'tutorial'}

#tags in tags_one but not thos that are in tags_two
exclusive_to_tags_one = tags_one - tags_two
print(exclusive_to_tags_one) #>{'python'}

#tags in tags_two but not in tags_one
exclusive_to_tags_two = tags_two -tags_one
print(exclusive_to_tags_two)#>{'ruby', 'development'}

#tags in both tag´s sets, those that are shared by both

shared_tags = tags_one & tags_two
print(shared_tags) #>{'tutorial', 'CODING'}