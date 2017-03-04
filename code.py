def create_cook_book(name_of_file):  
    length = sum(1 for string in open(name_of_file, 'r'))
    with open(name_of_file) as products:
        number = 0
        dishes = []
        cook_book = {}
        while number < length:  
            dish = products.readline().strip()
            dishes.append(dish)
            number += 1
            ingridients = int(products.readline().strip())
            number += 1
            cook_book[dish] = []
            
            for ingridient in range(ingridients):
                product_name, product_kol, product_measure = (products.readline().strip()).split(' | ')
                product_kol = int(product_kol)
                number += 1
                cook_book[dish].append({'ingridient_name' : product_name, 'ingridient_count' : product_kol, 'ingridient_measure' : product_measure})
        return dishes, cook_book
            
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['ingridient_count'] *= person_count

            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['ingridient_count'] += new_shop_list_item['ingridient_count']
                
    print('Список покупок') 
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['ingridient_count'], shop_list_item['ingridient_measure'].strip()))

person_count = int(input('Введите количество человек: '))
dishes, cook_book = create_cook_book('product.txt')
print('Введите заказ в одной строке через пробел')
dishes_that_persons_want = input().split()
get_shop_list_by_dishes(cook_book, dishes_that_persons_want, person_count)


