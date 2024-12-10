import unittest
from unittest.mock import patch
from rental.product import Product
from rental.product_data import product_data
from datetime import datetime

class TestProduct(unittest.TestCase):
    def test_constructor(self):
        product = Product(
            product_id='Y8786',
            product_name="White Striped Satin Linen Napkins", 
            description="5 Pack White Striped Satin Linen Napkins, Wrinkle-Free Reusable Wedding Napkins - 20'x20'", 
            quantity=500, 
            price=3.99,
            availability=['08/12/2026', '04/01/2026', '09/19/2026', '10/29/2025', '12/13/2024', '12/14/2024']
            )
        self.assertEqual(product.product_id, 'Y8786')  
        self.assertEqual(product.product_name, 'White Striped Satin Linen Napkins')
        self.assertEqual(product.description, "5 Pack White Striped Satin Linen Napkins, Wrinkle-Free Reusable Wedding Napkins - 20'x20'")
        self.assertEqual(product.quantity , 500)
        self.assertEqual(product.price, 3.99)
        self.assertEqual(product.availability, ['08/12/2026', '04/01/2026', '09/19/2026', '10/29/2025', '12/13/2024','12/14/2024',])
        self.assertEqual(product.user_quantity, 0)
    
    def test_update_quantity_valid_input(self):
        product = Product(
            product_id='Y8786',
            product_name="White Striped Satin Linen Napkins", 
            description="5 Pack White Striped Satin Linen Napkins, Wrinkle-Free Reusable Wedding Napkins - 20'x20'", 
            quantity=500, 
            price=3.99,
            availability=['08/12/2026', '04/01/2026', '09/19/2026', '10/29/2025', '12/13/2024', '12/14/2024']
            )
        mock_stock_quantity = 500
        mock_user_quantity = 300
        stock_quantity, user_quantity = product.update_quantity(mock_stock_quantity, mock_user_quantity)
    
        self.assertEqual(stock_quantity, 200)
        self.assertEqual(user_quantity, 300)


        #valid Input - when user quantity is greater than stock quantity
        mock_stock_quantity = 25
        mock_user_quantity = 70
        with self.assertRaises(ValueError):
            product.update_quantity(mock_stock_quantity, mock_user_quantity) 
    
    def test_available(self):
        product = Product(
            product_id='Y8786',
            product_name="White Striped Satin Linen Napkins", 
            description="5 Pack White Striped Satin Linen Napkins, Wrinkle-Free Reusable Wedding Napkins - 20'x20'", 
            quantity=500, 
            price=3.99,
            availability=['08/12/2026', '04/01/2026', '09/19/2026', '10/29/2025', '12/13/2024', '12/14/2024']
            )
        #when date is available
        mock_rental_date = datetime.strptime("01/01/2029", "%m/%d/%Y")
        self.assertTrue(product.available(mock_rental_date))
        
        #when date is not available
        mock_rental_date = datetime.strptime("12/13/2024", "%m/%d/%Y")
        self.assertFalse(product.available(mock_rental_date))
        
    def test_update_availability(self):
        product = Product(
            product_id='Y8786',
            product_name="White Striped Satin Linen Napkins", 
            description="5 Pack White Striped Satin Linen Napkins, Wrinkle-Free Reusable Wedding Napkins - 20'x20'", 
            quantity=500, 
            price=3.99,
            availability=['08/12/2026', '04/01/2026', '09/19/2026', '10/29/2025', '12/13/2024', '12/14/2024']
            )
        mock_rental_date = datetime.strptime("01/01/2029", "%m/%d/%Y")
        mock_quantity = 20
        result = product.update_availability(mock_rental_date, mock_quantity)
        self.assertTrue(result)
        self.assertEqual(product.quantity, 480)
        
        #when date is available but stock quantity is not enough
        mock_rental_date = datetime.strptime("01/01/2029", "%m/%d/%Y")
        mock_quantity = 950
        result = product.update_availability(mock_rental_date, mock_quantity)
        self.assertFalse(result)
        self.assertEqual(product.quantity, 480)
        
        #when date is not available but stock quantity is not enough
        mock_rental_date = datetime.strptime("12/14/2024", "%m/%d/%Y")
        mock_quantity = 700
        result = product.update_availability(mock_rental_date, mock_quantity)
        self.assertFalse(result)
        self.assertEqual(product.quantity, 480)
        
    def test_show_all_products(self): 
        product1 = Product(
            product_id='Y8786',
            product_name="White Striped Satin Linen Napkins", 
            description="5 Pack White Striped Satin Linen Napkins, Wrinkle-Free Reusable Wedding Napkins - 20'x20'", 
            quantity=500, 
            price=3.99,
            availability=['08/12/2026', '04/01/2026', '09/19/2026', '10/29/2025', '12/13/2024', '12/14/2024']
            )
        product2 = Product(
            product_id= 'P9666',
            product_name="Black Round Tablecloth", 
            description="120' Black Seamless Polyester Round Tablecloth for 5 Foot Table With Floor-Length Drop", 
            quantity=20, 
            price=9.19, 
            availability=['06/03/2025', '06/04/2025', '12/15/2024', '07/04/2025', '08/29/2025', '08/30/2025', '12/13/2024',]
            )
        
        mock_product_data = {product1: 'Y8786', product2: 'P9666'}
        with patch('rental.product_data', return_value=mock_product_data):
            all_products = product2.show_all_products()
            self.assertIn('P9666', all_products)
            self.assertIn('Y8786', all_products)
            
            #test if total of all products match
            self.assertEqual(len(all_products), 10)
            
            #testing to see if id and name matched and assume rest is true.
            self.assertEqual(all_products['P9666'].product_id, product2.product_id)
            self.assertEqual(all_products['P9666'].product_name, product2.product_name)
 
if __name__ == '__main__':
    unittest.main()