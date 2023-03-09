'''
В этом примере класс "Магазин" содержит четыре метода:
"add_product" (добавление товара),
"remove_product" (удаление товара),
"update_product_price" (изменение цены товара) и
"get_all_products" (вывод всех товаров в магазине).

Каждый товар представляется в виде пары "название: цена".
'''

class Shop:
    def __init__(self):
        '''Конструктор класса'''
        self.products = {}

    def __str__(self):
        return f'Наши продукты: {self.products}'

    def add_product(self, name:str, price:float):
        '''Добавление товара'''
        if name in self.products:
            print(f'{name.title()} уже имеется в магазине!')
        else:
            self.products[name] = price
            print(f'{name.title()} добавлен в магазин!')

    def remove_product(self, name:str):
        '''Удаление товара'''
        if name in self.products:
            del self.products[name]
            print(f'Товар {name} был удален!')
        else:
            print(f'Товара {name} нет в магазине!')

    def update_product_price(self, name:str, new_price:float):
        '''Обновление стоимости товара'''
        if name in self.products:
            self.products[name] = new_price
            print(f'Стоимость {name} изменена!')
        else:
            print(f'Товара {name} нет в магазине!')

    def get_all_products(self):
        '''Вывод всех товаров'''
        if self.products == {}:
            return f'В магазине нет товаров'
        else:
            return self.products.keys()

'''Создаем экземпляр класса.'''
shop = Shop()
'''Добавляем товары.'''
shop.add_product('молоко', 32.0)
shop.add_product('яблоки', 2.0)
shop.add_product('сыр', 12.0)
shop.add_product('курица', 22.0)
shop.add_product('апельсин', 11.0)
shop.add_product('рыба', 6.0)
print(shop)
'''Тестирую добавление товара, который уже есть в магазине. Проверка условия'''
shop.add_product('рыба', 7.0)
print(shop) ### Стоимость рыбы не изменилась, все верно!
'''Тестирую удаление товара, которого нет  и который есть в магазине. Проверка условия'''
shop.remove_product('икра')
shop.remove_product('рыба')
print(shop) ### Рыба удалилась.
'''Обновляю стоимость товара который есть и который отсутствует. Проверка работы условия'''
shop.update_product_price('молоко', 25.0)
shop.update_product_price('икра', 25.0)
print(shop) ### Икры в магазине нет. Обновить стоимость - нельзя. Стоимость молока изменена
'''Вывод всех товаров в магазине'''
print(shop.get_all_products())

products_list = shop.get_all_products() ### Этот момент подсмотрела.
for product in products_list:
    print(product)
