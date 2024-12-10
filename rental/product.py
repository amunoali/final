class Product():
    def __init__(self, product_id, product_name, description,  quantity, price, availability=None):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.quantity = quantity
        self.user_quantity = 0
        self.price = price
        self.availability = availability if availability else []

    def update_quantity(self, stock_quantity, user_quantity):
        #take in item, 
        if stock_quantity < user_quantity:
            raise ValueError(f'Unavailable, we have {stock_quantity} left in stock.')
            #updating user quanitity 
        self.user_quantity += user_quantity
            #updatng store quantity 
        stock_quantity -= user_quantity
        if stock_quantity <= 0:
            raise ValueError('We do not have enough stock, please select a different item')            
        elif self.user_quantity < 0:
            raise ValueError('You cannot have a negative number for quanity')
        return stock_quantity, user_quantity
        
    def show_all_products(self):
        from rental.product_data import product_data
        all_products = product_data()
        return all_products
    
    def available(self, rental_date):
        #convert rental date to string
        convert_rental_date = rental_date.strftime("%m/%d/%Y")
        if convert_rental_date in self.availability:
            return False
        return True
    
    def update_availability(self, rental_date, quantity):
        #convert rental date to string
        convert_rental_date = rental_date.strftime("%m/%d/%Y")
        #if items is available, update stock quantity. 
        if self.available(rental_date):
            if self.quantity >= quantity:
                self.quantity -= quantity
                return True
            else:
                print('Not enough stock available')
                return False
        else:
            print(f'{self.product_name} is not available on {convert_rental_date}')
            return False
    
    def __str__(self):
        return f'{self.product_id} {self.product_name} \n {self.description} \n {self.quantity} \n {self.user_quantity} \n {self.price} \n {self.availability}  '
