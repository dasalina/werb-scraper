import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/David/PycharmProjects/Scraper/chromedriver.exe')
driver.get('https://www.acefitness.org/resources/everyone/blog/')
titles_list = []
dates_list = []
authors_list = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

for a in soup.findAll(attrs='post-preview'):
    name = a.find('h2')
    if name not in titles_list:
        titles_list.append(name.text)

for b in soup.findAll(attrs='post-preview__meta'):
    date = b.find('time')
    if date not in dates_list:
        dates_list.append(date.text)

for c in soup.findAll(attrs='post-preview__meta'):
    author = c.find('span')
    if author not in authors_list:
        authors_list.append(author.text)

df = pd.DataFrame({'Names': titles_list, 'Dates':dates_list, 'Author':authors_list})
df.to_csv('names.csv', index = False, header = True, sep = ',', encoding = 'utf-8')
