# Необходимо написать программу для кулинарной книги.
# Список рецептов должен храниться в отдельном файле в следующем формате:
# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения

from pprint import pprint

import os

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='utf-8') as file:

    cook_book = {}

    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        list_of_ingredient = []

        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            list_of_ingredient.append(
                {'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
            )
        cook_book[dish_name] = list_of_ingredient
        file.readline()
        
    print('cook_book:')    
    pprint(cook_book)