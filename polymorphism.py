# polymorphism without inheritance

class Heading:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f' <h1>{self.content}</h1>'

class Div:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<div>{self.content}</div>'


div_one = Div('Some Content')
heading = Heading('Some Big Heading')
div_two = Div('Anoher div')

def html_render(tag_object):
    print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)
