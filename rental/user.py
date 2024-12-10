import phonenumbers
import re

class User():
    def __init__(self, first_name, last_name, email, phone, location):
        self.user_id = email
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.location = location
        
    def validate_first_name(self):
        self.first_name = input("First Name: ")
        #verify if user enters anything less than 2 characters, numbers, and if its not string
        while not isinstance(self.last_name, str) or len(self.first_name) <=2 or not self.first_name.isalpha():
            self.first_name = input("Invalid, please enter your first name: ")
        return self.first_name
                
    def validate_last_name(self):
        self.last_name = input("Last Name: ")
        while not isinstance(self.last_name, str) or len(self.last_name) <=2 or not self.last_name.isalpha():
            self.last_name = input("Invalid, please enter your last name: ")
        return self.last_name
    
    def validate_email(self,):
        self.email = input("Email Address- format xxx@xxx.xx: ")
        #checks if match format: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        is_valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email)
        while not is_valid:
            try:
                self.email = input("Invalid Email Address- format xxx@xxx.xx: ")
                is_valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email)
            except TypeError:
                print('Invalid, email must characters')     
        return self.email   

    def validate_phone(self,):
        self.phone = input("Phone Number: ")
        while len(self.phone) != 10:
            try:
                self.phone = input("Phone Number must be 10 digits long: ")
            except TypeError:
                    print('Invalid, phone number must be an int')
        if len(self.phone) == 10:
            # learn to use package from: https://pypi.org/project/phonenumbers/
            number = phonenumbers.parse(self.phone, "US")
            national_format = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
            # print('national_format', national_format)
            self.phone = national_format
            return national_format
         

    def validate_location(self):
        while True:
            self.location = input('Where will your venue take place? Enter city: ')
            self.location = self.location
            if len(self.location) > 2 and all(word.isalpha() for word in self.location.split()):
                city = self.location.split()
                #if its one word or two words
                if len(city) == 1 or (len(city) == 2 and all(word.isalpha() for word in city)):
                    return city
                else:
                    print('Invalid, enter a proper city')
            else:
                print('Invalid, has to be more than 2 characters')

    def __str__(self):
        return f'{self.first_name} {self.last_name} \n {self.email} \n {self.phone} \n Venue location: {self.location} '
    

