def create_cook_book(name_of_file):  
    with open(name_of_file) as products:
        menu = products.readlines()
        kolichestvo = 0
        dishes = []
        cook_book = {}
        
        while kolichestvo < len(menu):  
            menu[kolichestvo] = menu[kolichestvo].strip()
            dish = menu[kolichestvo]
            dishes.append(dish)
            kolichestvo += 1
            ingridients = int(menu[kolichestvo])
            kolichestvo += 1
            cook_book[dish] = []
            
            for ingridient in range(ingridients):
                s = menu[kolichestvo]
                product_name,product_kol,product_measure = menu[kolichestvo].split(' | ')
                product_kol = int(product_kol)
                kolichestvo += 1
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
dishes_that_persons_want = list(input().split())
get_shop_list_by_dishes(cook_book, dishes_that_persons_want, person_count)


