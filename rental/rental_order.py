from rental.product import Product
from rental.user import User
from rental.rent_item import Rental_item


class Rental_order():
    def __init__(self, user, ): 
        self.user = user
        self.order = {}
        self.total_cost = {}

    def add_to_cart(self, user, selected_item, product_id, quantity, rental_date):
        #when user's doesn't have an order
        if user.user_id not in self.order:
            self.order[user.user_id] = []
            self.total_cost[user.user_id] = 0
        #if user order exists, only update quanity based on date selected
        if selected_item.available(rental_date):
            item_exists = False
            for item in self.order[user.user_id]:
                #check if rental item and date match, then update quantity
                if item.selected_item.product_id == product_id and item.rental_date == rental_date:
                    item.selected_item.user_quantity += quantity
                    item_exists = True
                    break
            #if item doesnt exist, add
            if not item_exists:
                cart_item = Rental_item(selected_item, quantity, rental_date)
                self.order[user.user_id].append(cart_item)
            #update product availability
            selected_item.update_quantity(selected_item.quantity, quantity)
            selected_item.update_availability(rental_date, quantity)
            print(f"Added {quantity} {selected_item.product_name} to your cart for {(rental_date).strftime("%m/%d/%Y")}.")
        else:
            print(f"Sorry, {selected_item.product_name} is not available on {(rental_date).strftime("%m/%d/%Y")}.")

    def total(self, user):
        total_amunt = 0
        for cart_item in self.order[user.user_id]: 
            #update total   
            total_amunt += cart_item.selected_item.price * cart_item.selected_item.user_quantity
        #store in total_cost attribute
        self.total_cost[user.user_id] = total_amunt
        return self.total_cost[user.user_id]

      
    def show_cart(self, user, ):
        #checks if order is greater than 0
        if user.user_id in self.order and len(self.order) > 0:
            #for every order user has, print it.
            for cart_item in self.order[user.user_id]:
                product = cart_item.selected_item
                print(f'{product.product_name}, ${product.price}, quantity {product.user_quantity} on {(cart_item.rental_date).strftime("%m/%d/%Y")}')
            #Rounded to 2 decimal place 
            total = round(self.total(user), 2)
            return total
        else:
            print(f'{user.user_id}, your cart is empty')