"""
Esse módulo faz chamadas básicas no site https://realpython.github.io/fake-jobs/.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL,timeout=10)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title is-5")
    company_element = job_element.find("h3", class_="subtitle is-6 company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
