import itertools
import urllib.request as r
import json
import pandas as pd
from bs4 import BeautifulSoup

def req_url():
  data = r.urlopen(URL).read().decode()
  soup = BeautifulSoup(data, features="html.parser")
  data_file = open("data.txt", "w")
  data_file.write(str(soup))

def fetch(x):
  BASE_URL = "https://www.rei.com"
  data = r.urlopen(f'https://www.rei.com/c/hiking-backpacks?page={x}').read().decode()
  soup = BeautifulSoup(data, "html.parser")
  results = [BASE_URL + link.attrs["href"] for link in soup.select("#search-results > ul > li > a")]
  return list(dict.fromkeys(results))

def parse_product(url):
  data = r.urlopen(url)
  soup = BeautifulSoup(data, "html.parser")
  details = soup.select('script[type="application/ld+json"]', limit=1)
  return json.loads(details[0].text)

def main():
  urls = [fetch(x) for x in range(1, 3)]
  products = list(itertools.chain.from_iterable(urls))
  return [parse_product(url) for url in products]

if __name__ == '__main__':
  html_doc = open("data.txt", "r")
  URL = "https://www.rei.com/c/hiking-backpacks?page=1"
  df = pd.json_normalize(main())
  df.to_csv('rei-backpacks.csv', index=False)
  print('finished.')