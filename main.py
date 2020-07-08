# import sys
# sys.path.insert(0, './libs')
# import helper

# def render():
#     print(helper.greeting('Elizabeth', 'Martinez'))

# render()

# Import a n specific function

# import sys
# sys.path.insert(0, './libs')
# from helper import greeting

# def render():
#     print(greeting('Elizabeth', 'Martinez'))

# render()


#import and assign an alias 

import sys
sys.path.insert(0, './libs')
import helper as h

def render():
    print(h.greeting('Elizabeth', 'Martinez'))

render()

