cook_book = {}
with open('recipes.txt', 'rt', encoding="utf-8") as file:
    for l in file:
        dish_name = l.strip()
        ingredients = []
        dish = {dish_name: ingredients}
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingred = file.readline()
            ingredient_name, quantity, measure = ingred.strip().split(' | ')
            ingredients.append({"ingredient_name": ingredient_name,
                                        "quantity": quantity,
                                        "measure": measure})
        blank_line = file.readline()
        cook_book.update({dish_name: ingredients})

print(f'cook_book = {cook_book}')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for d in dishes:
        if d in cook_book.keys():
            for ingredient in cook_book[d]:
                person_quantity = ingredient['quantity'] * person_count
                shop_list.update({ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}})
    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 3))


def number_of_line(*files):
    lines = {}
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            lines.update({file: len(file_obj.readlines())})

    new_lines = {}
    for i in sorted(lines, key=lines.get):
        new_lines[i] = lines[i]
    return new_lines


number_of_line('1.txt', '2.txt', '3.txt')


def write_file(*files):
    text_dict = {}
    for i in number_of_line(*files):
        with open(i, encoding='utf-8') as file_obj:
            f = file_obj.read()
            text_dict.update({i: f})
    for key, value in text_dict.items():
        with open('final.txt', 'a', encoding='utf-8') as file:
            file.writelines([f"{key}\n{number_of_line(*files)[key]}\n{value}\n"])


print(write_file('1.txt', '2.txt', '3.txt'))


