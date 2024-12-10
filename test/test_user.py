import unittest
from rental.user import User
from unittest.mock import patch

class TestUser(unittest.TestCase):
    def test_constructor(self):
        test_user = User('Naima', 'Ali', 'naima.ali@gmail.com', '123-456-7890', 'Portland')

        self.assertEqual(test_user.first_name, 'Naima')
        self.assertEqual(test_user.last_name,'Ali')
        self.assertEqual(test_user.email, 'naima.ali@gmail.com')
        self.assertEqual(test_user.phone, '123-456-7890')
        self.assertEqual(test_user.location, 'Portland')
        
    def test_validate_first_name(self):
        #Valid Input
        with patch('builtins.input', return_value='Bob'):
            user = User(first_name='Bob', last_name='Jenkin', email='jenny@icloud.com', phone='555-555-5555', location='Boston')
            first_name = user.validate_first_name() 
            self.assertEqual(first_name, 'Bob')
        

        # Invalid inputs when user enters words less than 2 characters and then valid input
        with patch('builtins.input', side_effect=['B', 'bo', 'Bob']):
            first_name = user.validate_first_name()
            self.assertNotEqual(first_name, 'B')
            self.assertNotEqual(first_name, 'bo')
            self.assertEqual(first_name, 'Bob')

        #Invalid inputs when user enters numbers or special characters
        with patch('builtins.input', side_effect=['567', '{[876hjg', '$%Agj', 'Bob']):
            first_name = user.validate_first_name()
            self.assertNotEqual(first_name, '567')
            self.assertNotEqual(first_name, '{[876hjg')
            self.assertNotEqual(first_name, '$%Agj')
            self.assertEqual(first_name, 'Bob')
   
    def test_validate_last_name(self):
        #Valid input
        with patch('builtins.input', return_value='Hassan'):
            user = User(first_name='Salmah', last_name='Hassan', email='Salmah@icloud.com', phone='345-475-5234', location='Westbrook')
            last_name = user.validate_last_name()
            self.assertEqual(last_name, 'Hassan')

        # Invalid inputs when user enters words less than 2 characters and then valid input
        with patch('builtins.input', side_effect=['k', 'lk', 'Hassan']):
            last_name = user.validate_last_name() 
            self.assertNotEqual(last_name, 'k')
            self.assertNotEqual(last_name, 'lk')
            self.assertEqual(last_name, 'Hassan')
        
        #Invalid inputs when user enters numbers or special characters
        with patch('builtins.input', side_effect=['000', '89[0]', 'hghj7','Hassan']):
            last_name = user.validate_last_name() 
            self.assertNotEqual(last_name, '000')
            self.assertNotEqual(last_name, '89[0]')
            self.assertNotEqual(last_name, 'hghj7')
            self.assertEqual(last_name, 'Hassan')
   
    def test_validate_email(self):
        #valid input
        with patch('builtins.input', return_value='kanza@gmail.com'):
            user = User(first_name='Kanza', last_name='Hassan', email='kanza@gmail.com', phone='207-167-1235', location='Boston')
            email = user.validate_email()
            self.assertEqual(email, 'kanza@gmail.com')

        # Invalid inputs -incorrect format
        with patch('builtins.input', side_effect=['koiui', 'lkj@', 'sdf@d.', 'kanza@gmail.com']):
            user = User(first_name='Kanza', last_name='Hassan', email='kanza@gmail.com', phone='207-167-1235', location='Boston')
            email = user.validate_email()
            self.assertNotEqual(email, 'koiui')
            self.assertNotEqual(email, 'lkj@')
            self.assertNotEqual(email, 'sdf@d.')
            self.assertEqual(email, 'kanza@gmail.com')
   
    def test_validate_phone(self):
        #valid input
        with patch('builtins.input', return_value='(207)-167-1235'):
            user = User(first_name='Kanza', last_name='Hassan', email='kanza@gmail.com', phone='207-167-1235', location='Boston')
            phone = user.validate_phone()
            self.assertEqual(phone, '207-167-1235')

        # Invalid inputs -incorrect format
        with patch('builtins.input', side_effect=['443dsf4', '434.334.3423', '12345678901', '207-167-1235']):
            phone = user.validate_phone()
            self.assertNotEqual(phone, '443dsf4')
            self.assertNotEqual(phone, '434.334.3423')
            self.assertNotEqual(phone, '12345678901')
            self.assertEqual(phone, '207-167-1235')

    def test_validate_location(self):
        #valid input - one word city
        with patch('builtins.input', return_value = 'Portland'):
            user = User(first_name='Alice', last_name='Abdi', email='alice@icloud.com', phone='207-678-1234', location='Portland')
            location = user.validate_location()  
           
            self.assertEqual(location, ['Portland']) 
        #valid input two word city
        with patch('builtins.input', return_value = 'South Boston'):
            user = User(first_name='Alice', last_name='Abdi', email='alice@icloud.com', phone='207-678-1234', location='South Boston')
            location = user.validate_location()  
            self.assertEqual(location, ['South', 'Boston']) 
       
       #invalid
        with patch('builtins.input', side_effect=['1234', '!!InvalidCity', 'New York']):
            user = User(first_name='Alice', last_name='Abdi', email='alice@icloud.com', phone='207-678-1234', location='New York')
            location = user.validate_location()  
            self.assertNotEqual(location, '1234')
            self.assertNotEqual(location, '!!InvalidCity')
            self.assertEqual(location, ['New', 'York']) 
    

if __name__ == '__main__':
    unittest.main()