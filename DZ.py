with open('recipes.txt', 'r') as rec_list:
    cook_book = {}
    for line in rec_list:
        dish_name = line.strip()
        rec = {dish_name: []}
        ingredients_count = rec_list.readline()
        for i in range(int(ingredients_count)):
            ingredient = rec_list.readline()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            dish_ingredient = {"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure.strip()}
            rec[dish_name].append(dish_ingredient)
        rec_list.readline()
        cook_book.update(rec)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:  # перебираем список блюд для покупки
        for ingredient in cook_book[dish]:    # выводим ингредиенты для блюд
            ingredient_list = dict([(ingredient["ingredient_name"], {'measure': ingredient["measure"], 'quantity': int(ingredient["quantity"])*person_count})])
            if shop_list.get(ingredient["ingredient_name"]):
                multi_ingredient = shop_list[ingredient["ingredient_name"]]["quantity"] + ingredient_list[ingredient["ingredient_name"]]["quantity"]
                shop_list[ingredient["ingredient_name"]]["quantity"] = multi_ingredient
            else:
                shop_list.update(ingredient_list)
    print(shop_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)