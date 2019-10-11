import os
from tqdm import tqdm

from bs4 import BeautifulSoup

for filename in tqdm(os.listdir('data')):
    if filename.endswith(".html"):
        page = open(os.path.join('data', filename), encoding="cp1251")
        soup = BeautifulSoup(page.read(), "html.parser")
        articles = soup.findAll('article')
        for article in articles:
            h2s = article.findAll('h2')
            for h2 in h2s:
                urls = h2.findAll('a', href=True)
                for url in urls:
                    with open('links.txt', 'a') as file:
                        file.write(url['href'] + '\n')