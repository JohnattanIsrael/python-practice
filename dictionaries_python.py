# players = {
#     'ss': 'Correa',
#     '2b': 'Altuve',
#     '3b': 'Bregman',
#     'DH': 'Gattis',
#     'OF': 'Springer'
# }

# second_base = players['2b']
# print(second_base) #> Altuve

# designated_hitter = players['DH']
# print(designated_hitter) #> Gattis

# designated_hitter = players['dh']
# print(designated_hitter) #> KeyError: 'dh'

# teams = {
#     'astros':['Altuve', 'Correa', 'Bregman'],
#     'angels':['Trout', 'Pujols'],
#     'Yankees':['Judge', 'Stanton']
# }
# print(teams['astros'])#>['Altuve', 'Correa', 'Bregman']
# print(teams['astros'][:2])#>['Altuve', 'Correa']

# beisball_teams = teams
# print(teams)

# astros = teams['astros']

# print(astros)

# print(teams['Yankees'])

# teams = {
#     'astros':['Altuve', 'Correa', 'Bregman'],
#     'angels':['Trout', 'Pujols'],
#     'Yankees':['Judge', 'Stanton']
# }
# teams['red sox'] = ['Price,' 'Betts']

# print(teams) #>{'astros': ['Altuve', 'Correa', 'Bregman'], 'angels': ['Trout', 'Pujols'], 'Yankees': ['Judge', 'Stanton'], 'red sox': ['Price,Betts']}

# # THE FOLLOWING IS A BEST PRACTICE
# teams = {
#     'astros':['Altuve', 'Correa', 'Bregman'],
#     'angels':['Trout', 'Pujols'],
#     'Yankees':['Judge', 'Stanton'],
#     'red sox':['Price', 'Betts']
# }

# feature_team = teams.get('mets', 'No feature team')
# # the first argment declares what are you looking for in the dictionary and the second definds whats happens if it does not find the keyvalue
# print(feature_team) #> No feature team

# players = {
#     'ss': 'Correa',
#     '2b': 'Altuve',
#     '3b': 'Bregman',
#     'DH': 'Gattis',
#     'OF': 'Springer'
# }

# print(players.keys()) #> dict_keys(['ss', '2b', '3b', 'DH', 'OF'])
# print(players.values()) #> dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])
# print(players.items()) #>dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])
# # dict.values does not support indexing, so you canot treat them like a traditional list

# print(list(players.values())[1]) #>Altuve 
# #in the pas case , it is risky because of the dynamic characteristic of the dictionary view objects because someone could change the values while you are working on them
# #so you can create a copy using the copy(). function 
# player_names = list(players.copy().values())
# print(player_names)

# teams = {
#     'astros':['Altuve', 'Correa', 'Bregman'],
#     'angels':['Trout', 'Pujols'],
#     'Yankees':['Judge', 'Stanton'],
#     'red sox':['Price', 'Betts']
# }

# team_groupings = teams.items()

# print(team_groupings)# dict_items([('astros', ['Altuve', 'Correa', 'Bregman']), ('angels', ['Trout', 'Pujols']), ('Yankees', ['Judge', 'Stanton']), ('red sox', ['Price', 'Betts'])])
# """
# dict_items
# (
#     [
#         ('astros', ['Altuve', 'Correa', 'Bregman']),
#         ('angels', ['Trout', 'Pujols']),
#         ('Yankees', ['Judge', 'Stanton']),
#         ('red sox', ['Price', 'Betts'])
#     ]
# )
# """

# print(len(team_groupings))#>4

# print(list(team_groupings)[1]) #> ('angels', ['Trout', 'Pujols'])

# print(list(team_groupings)[1][1]) #> ['Trout', 'Pujols']

# print(list(team_groupings)[1][1][0]) #> Trout

# print(('astros', ['Altuve', 'Correa', 'Bregman']) in team_groupings) #>true

# print(('mets',['some', 'guy']) in team_groupings)#> False


# teams = {
#     'astros':['Altuve', 'Correa', 'Bregman'],
#     'angels':['Trout', 'Pujols'],
#     'Yankees':['Judge', 'Stanton'],
#     'red sox':['Price', 'Betts']
# }

# del teams['astros'] #if I try to print out the key 'mets' which does´nt exists it will return an error so you can better pop it

# print(teams) #>{'angels': ['Trout', 'Pujols'], 'Yankees': ['Judge', 'Stanton'], 'red sox': ['Price', 'Betts']}

# teams.pop('Yankees', 'No team found by that name')
# print(teams) #>{'astros': ['Altuve', 'Correa', 'Bregman'], 'angels': ['Trout', 'Pujols'], 'red sox': ['Price', 'Betts']}
# teams.pop('Mets', 'No team found by that name')
# # Pop to be printed out has to be stored inside a variable
# removed_team = teams.pop('red sox' ,'No team found by that name')
# print(teams) #>{'astros': ['Altuve', 'Correa', 'Bregman'], 'angels': ['Trout', 'Pujols'], 'Yankees': ['Judge', 'Stanton']}
# print(removed_team) #>['Price', 'Betts']

# removed_team_two = teams.pop('Mets' ,'No team found by that name')
# print(removed_team_two) #> No team found by that name

