import requests
from bs4 import BeautifulSoup
import inflection

URL = 'http://www.dailysmarty.com/topics/python/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

for post in soup.find_all(class_='post-link-title'):
    for title_wrapper in post.find_all('h2'):
        title_in_text = f'h2-----the title should be the following => {title_wrapper.text} <='
    # print(title_in_text)
    links = []
    for links in title_wrapper('a'):
        links.append(links.get('href'))
    # print(f'Link..............{links}')
    for title_url in title_wrapper.find_all('a', href=True):
        url = (title_url['href'])
        length = (len(title_url['href']))
        unformatted_title = (title_url['href'][7:])
        # print(url)
        # print(length)
        # print(unformatted_title)
        print(inflection.titleize(unformatted_title))




