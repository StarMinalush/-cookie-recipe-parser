import os
from tqdm import tqdm
from bs4 import BeautifulSoup
import csv

with open('recipes.csv', mode='a') as csv_file:
    fieldnames = ['name', 'ingredients', 'recipe', 'appointment', 'tags', 'tastes']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for filename in tqdm(os.listdir('pages')):
        if filename.endswith(".html"):
            page = open(os.path.join('pages', filename), encoding="cp1251")
            soup = BeautifulSoup(page.read(), "html.parser")
            recipe_name = soup.find('div', itemscope='', itemtype="http://data-vocabulary.org/Recipe").find('h1').contents[0]
            ingredients_tag =soup.find('div', itemscope='', itemtype="http://data-vocabulary.org/Recipe").find('div', class_='ingredients-bl').find('ul').findAll('li')
            ingredients = list()
            for ingredient in ingredients_tag:
                name = ingredient.find('span', itemprop='name').contents[0]
                amount_tag = ingredient.find('span', itemprop='amount')
                if amount_tag:
                    amount = amount_tag.contents[0]
                else:
                    amount = None
                ingredients.append((name, amount))
            recipe_text_tags =soup.find('div', itemscope='', itemtype="http://data-vocabulary.org/Recipe").findAll('div', class_='cooking-bl', itemprop="recipeInstructions")
            recipe = ""
            for tag in recipe_text_tags:
                recipe +=tag.find('div').find('p').contents[0]
            recipe_tags_tags = soup.find('div', itemscope='', itemtype="http://data-vocabulary.org/Recipe").find('div', class_='article-tags', id="tags-recipes-01").findAll('p')
            appointment = list()
            tags = list()
            tastes = list()
            appointment_items = recipe_tags_tags[0].findAll('a')
            tags_items = recipe_tags_tags[1].findAll('a')
            tastes_items = recipe_tags_tags[2].findAll('a')
            for i in appointment_items:
                appointment.append(i.contents[0])
            for i in tags_items:
                tags.append(i.contents[0])
            for i in tastes_items:
                tastes.append(i.contents[0])

            writer.writerow({'name': recipe_name, 'ingredients': ingredients, 'recipe': recipe, 'appointment':appointment, 'tags':tags, 'tastes':tastes})

