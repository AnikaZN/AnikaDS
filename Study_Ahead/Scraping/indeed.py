import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.indeed.com/jobs?q=Data+Scientist&l=Utah")
response_html = response.text

soup = BeautifulSoup(response_html, features = 'lxml')

listings = soup.find_all('div', 'jobsearch-SerpJobCard')

jobs = []
for list_item in listings:
    title = list_item.find('div', 'title').text
    company = list_item.find('span', 'company').text
    description = list_item.find('div', 'summary').text
    job = {'title': title, 'company': company, 'description': description}
    jobs.append(job)

print(jobs[3]['company'])
