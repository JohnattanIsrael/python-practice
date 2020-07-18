# INSTANCE ATTRIBUTE

# class Website:
#     def __init__(self, title):
#         self.title = title

# ws = Website('My Website title')
# print(ws.title)
# print(ws.__dict__)

# ws_two = Website('Second Title')
# print(ws_two.__dict__)

# My Website title
# {'title': 'My Website title'}
# {'title': 'Second Ttle'}

# CLASS ATTRIBUTE - BECAUSE IS INSIDE THE CLASS

class DifferentWebsite:
    title = 'My Class Title'

dw = DifferentWebsite()
print(dw.__dict__)
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)

#{}
# My Class Title
# My Class Title