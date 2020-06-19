class Product(object):
    product_made = []   #empty list to know when new products are approved to be on sale
    print("No products exist at this time.")
    print()

    #initializing our inputs
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__sale = False
        print(self.__name + " " + "is now a Product.")
        Product.product_made.append(self)  #adding to our empty list

    #to-string-method
    def __str__(self):
        reply = self.__name + " " + "(" + self.__category + ")," + " " + "$" + str(self.__price) + "," + " " 
        if not self.__sale:
            reply += "[NOT YET FOR SALE]"
            
        else:
            reply += "[ON SALE NOW]"
        return reply

    #to place item on sale   
    def approve(self):
        if not self.__sale:
            self.__sale = True
            print(self)
        else:
            self.__sale = False

    #keeping track of products
    def all_products(self):
        pass
    @staticmethod
    def show_products():
        print()
        print("The following products exist:")
        
        for product in Product.product_made:
            print(product)
    def set_name(self, new_product):
        if new_product == self.__name:
            print("Warning: The product already has that name!")
        elif new_product == "":
            print("Warning: The product must have a name!")
        else:
            self.__name = new_product

            
    #checking the prices with new prices
    def set_price(self, new_price):
        if new_price == self.__price:
            print("Warning: The product already has that price!")
        elif new_price < 0:
            print("Warning: The product must have a positive price!")
        else:
            self.__price = new_price



class Luxury(Product):
    def __init__(self, name, category, price, markup, slogan):
        super().__init__(name,category, price)
        self.markup = float(markup)
        self.slogan = str(slogan)
        print("(It's a luxury good)")

        
    

    
class Greater(Product):            
    def __lt__(self, name, category, price):
        super().__lt__(price)
        return self.__price < other.__price
        
    def __eq__(self, name, category, price):
        super().__lt__(price)
        return self.__price == other.price


#Test code for Section 1
print("Let's create some products:")
car = Product("Cheap EV", "Car", 36200)
book = Product("Doors of Stone", "Book", 30)
banana = Product("Bluth Banana", "Fruit", 10)
book2 = Product("Oathbringer", "Book", 16)
#Bonus
melon = Luxury("Square Watermelon", "Fruit", 25, 8, "Taste the price")
car2 = Luxury("Tesla Model S", "Car", 65600, 1.25, "Goodluck getting one")


print()
print(car)
print(book)
print(banana)
print(book2)

#Test code for Section 2
print()
print("\nNow we put some of these products into the market:")
car.approve()
banana.approve()
book2.approve()


Product.show_products()

#Test code for Section 3
print("\nHere we test error cases. We should get 4 errors:")
car.set_name("")
car.set_name("Cheap EV")
car.set_name("Tesla Model 3")
car.set_price(-1)
car.set_price(36200)

#Test code for Section 4
print("\nFinally, we sort and show all products:")
Product.all_products.sort()
Product.show_products()







