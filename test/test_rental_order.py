import unittest
from rental.rental_order import Rental_order
from rental.user import User
from rental.product import Product
from datetime import datetime


class TestRental_order(unittest.TestCase):
    def test_constructor(self):
        user = User(first_name='Bob', last_name='Jenkin', email='jenny@icloud.com', phone='555-555-5555', location='Boston')
    
        rental = Rental_order(user)
        self.assertEqual(rental.user, user)

    def test_add_to_cart(self):
        user = User(first_name='Bob', last_name='Jenkin', email='jenny@icloud.com', phone='555-555-5555', location='Boston')
        
        product = Product(
            product_id='V9879',
            product_name="Olive Chair Sashes", 
            description="5 Pack Dusty Sage Green Polyester Chair Sashes - 6'x108'", 
            quantity=250, 
            price=3.19, 
            availability= ['12/15/2024', '12/16/2024', '12/24/2024', '12/25/2024',  '01/01/2025', '01/02/2025','12/13/2024', ]
            )
        
        rental_order = Rental_order(user)
        
        mock_rental_date = datetime.strptime("01/01/2029", "%m/%d/%Y")
        mock_quantity = 12
        rental_order.add_to_cart(user, product, product.product_id, mock_quantity, mock_rental_date)
        
        #user added one item to cart
        self.assertEqual(len(rental_order.order[user.user_id]), 1)
        cart_item = rental_order.order[user.user_id][0]
        self.assertEqual(cart_item.selected_item.product_id, 'V9879')
        self.assertEqual(cart_item.quantity, 12)
        

    def test_total(self):
        user = User(first_name='Bob', last_name='Jenkin', email='jenny@icloud.com', phone='555-555-5555', location='Boston')
       
        product = Product(
            product_id='V9879',
            product_name="Olive Chair Sashes", 
            description="5 Pack Dusty Sage Green Polyester Chair Sashes - 6'x108'", 
            quantity=250, 
            price=3.19, 
            availability= ['12/15/2024', '12/16/2024', '12/24/2024', '12/25/2024',  '01/01/2025', '01/02/2025','12/13/2024', ]
            )
        
        rental_order = Rental_order(user)
        
        mock_rental_date = datetime.strptime("01/01/2027", "%m/%d/%Y")
        mock_quantity = 12
        rental_order.add_to_cart(user, product, product.product_id, mock_quantity, mock_rental_date)
        total = rental_order.total(user)
        expected_total = product.price * mock_quantity
        #testing if total and expected mach
        self.assertEqual(total, expected_total)
        
    def test_show_cart(self):
        user = User('Naima', 'Ali', 'naima.ali@gmail.com', '123-456-7890', 'Portland')
        product = Product(
            product_id='V9879',
            product_name="Olive Chair Sashes", 
            description="5 Pack Dusty Sage Green Polyester Chair Sashes - 6'x108'", 
            quantity=250, 
            price=3.19, 
            availability= ['12/15/2024', '12/16/2024', '12/24/2024', '12/25/2024',  '01/01/2025', '01/02/2025','12/13/2024', ]
            )
        rental_order = Rental_order(user)
        mock_rental_date = datetime.strptime("01/01/2027", "%m/%d/%Y")
        mock_quantity = 12
        rental_order.add_to_cart(user, product, product.product_id, mock_quantity, mock_rental_date)
        total = product.price * mock_quantity
        result = rental_order.show_cart(user)
        expected_result = total
        self.assertEqual(result, expected_result)
   
    #test when cart is empty
    def test_show_cart_empty(self):
        user = User('Naima', 'Ali', 'naima.ali@gmail.com', '123-456-7890', 'Portland')
        rental_order = Rental_order(user)
        result = rental_order.show_cart(user)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()