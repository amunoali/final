import unittest
from rental.rent_item import Rental_item
from rental.product import Product
from datetime import datetime



class TestRental_item(unittest.TestCase):
    def test_constructor(self):
        product = Product(
            product_id='V9879',
            product_name="Olive Chair Sashes", 
            description="5 Pack Dusty Sage Green Polyester Chair Sashes - 6'x108'", 
            quantity=250, 
            price=3.19, 
            availability= ['12/15/2024', '12/16/2024', '12/24/2024', '12/25/2024',  '01/01/2025', '01/02/2025','12/13/2024', ]
            )
        
        mock_rental_date = datetime.strptime("07/06/2025", "%m/%d/%Y")
        mock_quantity = 12
        item = Rental_item(product, mock_quantity, mock_rental_date) 
        self.assertEqual(item.selected_item, product)
        self.assertEqual(item.quantity, mock_quantity)
        self.assertEqual(item.rental_date, mock_rental_date)

    
    
if __name__ == '__main__':
    unittest.main()