import os
import random
import requests
import webbrowser

from bs4 import BeautifulSoup
from lxml import etree


with open("movies.json") as f:
    movies = json.load(f)

movie = random.choice(movies)

text = f'Seems like we are going to watch {movie} tonight'

q = f'smotret {movie} gidonline.io'

url = "https://www.google.com/search?q"

data = requests.get(f'{url}={q}').text

soup = BeautifulSoup(data, 'html.parser')

dom = etree.HTML(str(soup))

os.system(f"say {text}")

url = dom.xpath('//*[@id="main"]/div[3]/div/div[1]/a')[0].get('href')

url = f'https://www.google.com{url}'

webbrowser.open(url)
