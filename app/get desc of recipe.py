import requests
from tqdm import tqdm


num_lines = sum(1 for line in open('links.txt','r'))
counter = 0
with open('links.txt', 'r') as file:
    for url in tqdm(file, total=num_lines):
        r = requests.get(url)
        with open(f'pages/{counter}.html', 'w', encoding='cp1251') as output_file:
            output_file.write(r.text)
        counter +=1