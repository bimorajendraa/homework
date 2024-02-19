  
class Shop:
    
    def __init__(self, name, owner, address, products):
        self.name = name
        self.owner = owner
        self.address = address
        self.products = products

    def __str__(self):
        return self.name + " - " + self.address

    def add_product(self, product):
        self.products.append(product)

    def get_all_products(self):
        if len(self.products) > 0:
            for p in self.products:
                print("{0} - IDR. {1}".format(p.title, p.price))
        else:
            print("The shop has not products yet.")
    
    def get_product(self, id):
        pass


class Product:

    def __init__(self, id, title, price, quantity, description):
        self.id = id
        self.title = title
        self.price = price
        self.quantity = quantity
        self.description = description
    
    def discounted_price(self, discount):
        # homework
        pass

abc_shop = Shop(name="Toko ABC", owner="John Doe", address='Jalan Raya no 3', products=[])

print(abc_shop)


playstation_4 = Product(id=1, title='Playstation 4', price=4500000, quantity=4, description='A good gane console.')
vintage_gameboy = Product(id=2, title='Vintage GameBoy', price=800000, quantity=3, description='A vintage portable game')

#abc_shop.products.append(playstation_4)
#abc_shop.products.append(vintage_gameboy)

abc_shop.add_product(playstation_4)
abc_shop.add_product(vintage_gameboy)

print(abc_shop.products)
print(abc_shop.get_all_products())