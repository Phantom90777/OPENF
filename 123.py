def read_recipes(file_name):
    recipes = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            recipes[dish_name] = ingredients
            f.readline()  
    return recipes
if __name__ == "__main__":
    file_name = 'C:/Users/Леша/Desktop/OPENF/recipes.txt'
    cook_book = read_recipes(file_name)
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
    return shop_list


if __name__ == "__main__":
    file_name = 'recipes.txt'
    cook_book = read_recipes(file_name)

    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print(shop_list)

import os


def merge_files(file_names, output_file):
    file_info = []

    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            file_info.append((file_name, len(lines), lines))


    file_info.sort(key=lambda x: x[1])


    with open(output_file, 'w') as out_file:
        for file_name, line_count, lines in file_info:
            out_file.write(f"{file_name}\n{line_count}\n")
            out_file.writelines(lines)
            out_file.write('\n')

if __name__ == "__main__":
    file_names = ['recipes.txt']
    output_file = 'merged_file.txt'
    merge_files(file_names, output_file)


