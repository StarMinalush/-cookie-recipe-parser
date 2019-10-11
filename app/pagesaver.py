import requests
from tqdm import tqdm

for i in tqdm(range(1, 500)):
    url = f'https://www.povarenok.ru/recipes/~{i}/'  # get url
    r = requests.get(url)
    with open(f'data/{i}_page.html', 'w', encoding='cp1251') as output_file:
        output_file.write(r.text)
