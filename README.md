# netology
def create_cook_book():  
    products = open('product.txt','r')
    menu = products.readlines()
    kol = 0
    dishes = []
    cook_book = {}
    
    while kol < len(menu):  
        dish = menu[kol][:-1]
        dishes.append(dish)
        kol += 1
        ingridients = int(menu[kol])
        kol += 1
        cook_book[dish] = []
        
        for ingridient in range(ingridients):
            s = menu[kol]
            product_name = menu[kol][:s.find('|')-1]
            product_kol = int(menu[kol][s.find('|')+2:s.rfind('|')-1])
            product_measure = menu[kol][s.rfind('|')+2:-1]
            kol += 1
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
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['ingridient_count'], shop_list_item['ingridient_measure']))

person_count = int(input('Введите количество человек: '))
dishes, cook_book = create_cook_book()
get_shop_list_by_dishes(cook_book, dishes, person_count)


#Пример теста:
#omlette
#4
#eggs | 2 | sht
#carrot | 1 | sht
#cheese | 20 | gr
#salt | 1 | spoon
#fish
#2
#tunec | 1 | sht
#pepper | 3 | gr
#
