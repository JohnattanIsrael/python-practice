import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files: " , file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("Ruby files: " , file)
        
        if fnmatch.fnmatch(file, "*.yml"):
            print("Yaml files: " , file)

        if fnmatch.fnmatch(file, "*.py"):
            print("Python files: " , file)

# list_files()
# > Yaml files:  config.yml
# Python files:  file_matcher.py
# Ruby files:  scripts.rb
# Text files:  something.txt
# Text files:  something2.txt


players = [
    'Jose Altuve 2B',
    'Carlos Correa SS',
    'Alex Bregman #B',
    'Scooter Gennett 2B'
]

second_base_players = [player for player in players if fnmatchcase(player, '* 2B')]

print('players that play second base second_base_players', second_base_players)
#> players that play second base second_base_players ['Jose Altuve 2B', 'Scooter Gennett 2B']
