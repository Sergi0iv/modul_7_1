class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file1 = file.read()
        file.close()
        return file1

    def add(self, *products):
        current_products = self.get_products()

        for i in products:
            if str(i) not in current_products:
                file2 = open(self.__file_name, 'a')
                file4 = file2.write(f'\n{i}')
                file2.close()
                current_products += str(products) + '\n'
                return file4
            else:
                print(f'Продукт {str(i)} уже есть в магазине.')
                
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
