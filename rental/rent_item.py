class Rental_item():
    def __init__(self, selected_item, quantity, rental_date):
        self.selected_item = selected_item #references product 
        self.quantity = quantity
        self.rental_date = rental_date