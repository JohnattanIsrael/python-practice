# import requests
# from bs4 import BeautifulSoup
# from infelction import titlelize

# def titles_generator(links):
#     titles = []
    
#     def post_formatter(url):
#         if 'posts' in url:
#             url = url.split('/')[-1]
#             url = url.replace('-', ' ')
#             url = titlelize(url)
#             titles.append(url)
#     for link in links:
#         post_formatter(link['href'])

#     return titles

# r = requests.get('http://www.dailysmarty.com/topics/python/')
# soup = BeautifulSoup(r.text, 'html.parser')
# links = soup.find_all('a')

# titles = titles_generator(links)

# for title in titles:
#     print title

"""
the first time it did this =>
Traceback (most recent call last):
  File "web_scraper_jordan.py", line 21, in <module>
    print(titles_generator(links))
  File "web_scraper_jordan.py", line 13, in titles_generator
    post_formatter(link['href'])
  File "C:\Users\191141\AppData\Local\Programs\Python\Python38\lib\site-packages\bs4\element.py", line 1401, in __getitem__
    return self.attrs[key]
KeyError: 'href'
"""


# just to test
# for link in links:
#     print(link['href'])

# so this one is the right one

import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

# <!--- UPDATED CODE -->
    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))
# <!--- UPDATED CODE -->

    return titles


r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)