
import requests
from bs4 import BeautifulSoup
URL = 'https://www.monster.com/jobs/search/?q=Entry-Level-Software-Developer&where=Long-Beach__2C-CA'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

# for job_elem in job_elems:
#     print(job_elem, end = '\n'*2)

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
# to filter specific items look for the string argument
print('--------------')
# python_jobs = results.find_all('h2', string = 'Python Developer')

# print(python_jobs)#> it may have returned [] because the string argument is very strict with capitalization etc...
# so you can pass a function that can be more general
js_jobs = results.find_all('h2', string=lambda text: 'javascript' in text.lower())
print (f'there are {len(js_jobs)} jobs that match your search \n here they are=>')
# print(len(js_jobs))
for js_job in js_jobs:
    link = js_job.find('a')['href']
    print(js_job.text.strip())
    print(f'Apply here: {link}\n')

# <div id="SearchResults" class="mux-card mux-job-card">