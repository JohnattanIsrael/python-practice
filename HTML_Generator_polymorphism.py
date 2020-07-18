class HTML:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        raise NotImplementedError('Subclass must implement render method')

class Heading(HTML):
    def render(self):
        return f' <h1>{self.content}</h1>'

class Div(HTML):
    def render(self):
        return f'<div>{self.content}</div>'

tags = [
    Div('Some Content'),
    Heading('Some Big Heading'),
    Div('Anoher div')
]

for tag in tags:
    print(tag.render())
    # debugging content
    # print(str(tag) + ':' + tag.render())

#> <div>Some Content</div>
#  <h1>Some Big Heading</h1>
# <div>Anoher div</div>

# we have different behavior in the child classes because we override the 'render' value from the parent class
