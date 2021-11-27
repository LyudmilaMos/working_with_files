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

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}

    for dish in dishes:
       
        if dish in cook_book:    

            for list_of_ingredient in cook_book[dish]:

                if list_of_ingredient['ingredient_name'] not in shopping_list:
                    shopping_list[list_of_ingredient['ingredient_name']] = dict(measure=list_of_ingredient['measure'], quantity=int(
                        list_of_ingredient['quantity']) * person_count)
                else:
                    shopping_list[list_of_ingredient['ingredient_name']] = dict(measure=list_of_ingredient['measure'], 
                     quantity=int(
                        list_of_ingredient['quantity']) * person_count + 
                        shopping_list[list_of_ingredient['ingredient_name']].pop(
                        'quantity'))
        else:            
            return f'Неверно введено название блюда'

    return shopping_list

person_count = int(input('Введите количество персон: '))
dishes = input('Введите название блюд с большой буквы и через запятую из расчета на 1 персону: ') \
    .split(', ')
pprint(get_shop_list_by_dishes(dishes, person_count))