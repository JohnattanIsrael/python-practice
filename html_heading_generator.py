"""
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
  <h1>Generator</h1>
</body>
</html>
"""
def heading_generator(title, heading_type):
    return f'''<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>{title}</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
  <h1>{heading_type}</h1>
</body>
</html>'''

print(heading_generator('You did it bro', 'YOU ACTUALLY DID IT'))
print(heading_generator('hi there', '3'))

print('-----------')

def standard_form(name, lastname, email, phone):
    return f'''My name is {name} 
    please contact me at my email: {email}
    
    Or at my phone number {phone}

    thank you
    {name} {lastname}
    '''
print(standard_form('Mario', 'Pineda', 'email@email . com', '555 555 555'))



