import requests
from bs4 import BeautifulSoup

url = "https://ncatlab.org/nlab/show/higher+category+theory+and+physics"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.findAll('a', href=True)
with open('Davinci_Dataset.txt', 'w') as f:
  for link in links[2:1000]:
      if link['href'].startswith('/nlab/show/'):
          url = "https://ncatlab.org" + link['href']
          response = requests.get(url)
          soup = BeautifulSoup(response.text, 'html.parser')

          brain = {}
          for h2 in soup.findAll('h2', {'id': ['Idea', 'history', 'definition', 'Examples', 'properties', 'idea', 'BasicStructures', 'the_detailed_structures']}):
            for sibling in h2.find_next_siblings():
              if sibling.name == 'h2':
                break
              f.write(sibling.text)
              f.write('\n')