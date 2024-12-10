from rental.user import User
from rental.product import Product
from rental.rental_order import Rental_order
import datetime


def main():

    #user = User(first_name='mun', last_name='mun', email='cal@cal.co', phone='5555555555', location='boston')
    user = User(first_name='', last_name='', email='', phone='', location='')

    user.validate_first_name()
    user.validate_last_name()
    user.validate_email()
    user.validate_phone()
    user.validate_location()

    print('Welcome', user)
    validate_user_info = 'maybe'
    while validate_user_info != 'y':
        validate_user_info = input('Is all of your information correct: (y/n)').lower()
        if validate_user_info == 'n':
            print('Hello', user)
            update_user_info = input('which information is incorrect? \n first_name or last_name or email or phone or venue location (f, l, e, p, v): ')
            if update_user_info == 'f':
                user.validate_first_name()
                print('Hello', user)
            elif update_user_info == 'l':
                user.validate_last_name()
                print('Hello', user)
            elif update_user_info == 'e':
                user.validate_email()
                print('Hello', user)
            elif update_user_info == 'p':
                user.validate_phone()
                print('Hello', user)
            elif update_user_info == 'v':
                user.validate_location()
                print('Hello', user)
    print('Everything is correct', user.first_name)

    products = Product(
        product_id='',
        product_name='', 
        description='',
        quantity=0.0, 
        price=0.0, 
        availability=''
    )

    all_products = products.show_all_products()

    items_in_cart = Rental_order(user)

    product_selection = ''
    while product_selection != 'q':
           # prints all products in dictionary-count starting 1
        for index, (key, product) in enumerate(all_products.items(), start=1):
            print(index, ':', product.product_name, ' $', product.price)
        print('\n')
        product_selection = input('What items are you looking to rent: Enter the number associated \nOr enter q to quit: ')
        if product_selection == 'q':
            print('You selected:')
            print(f'Total Cost: ${items_in_cart.show_cart(user, )} \n')
            deposit_agreement = ('A non-refundable deposit of $200 is required to rental items. The deposit will go towards the total rental fee, with the remaining balance due 5 days prior to the event.')
            print(deposit_agreement)
            while True:
                try:
                    deposit = input('Do you agree with deposit agreement: y/n ').lower()
                    if deposit == 'y':
                        rental_agreement = (f'You agree to rent the specified items for {(rental_date).strftime("%m/%d/%Y")} and total fee of {items_in_cart.total(user)}. You are responsible for the care and return of all items, and any damages or missing items will incur additional charges.')
                        print(rental_agreement)
                        while True:
                            try:
                                rental = input('Do you agree with deposit agreement: y/n ').lower()
                                if rental == 'y':
                                    print('Thank you for your booking! Your rental is confirmed.')
                                    print('Your summary: \n ', user)
                                    print('Total Cost: $', items_in_cart.show_cart(user))
                                    break
                                elif rental == 'n':
                                    # print('You must agree to rental agreement') 
                                    
                                    cancel = input('Would you like to cancel your order: y/n ').lower()
                                    if cancel == 'y':
                                        print('Order Cancelled')                                        
                                        break
                                    elif cancel == 'n':
                                        rental = input('Do you agree with deposit agreement: y/n ').lower()
                                        if rental == 'y':
                                            print('Thank you for your booking! Your rental is confirmed.')
                                            print('Your summary: \n ', user)
                                            print('Total Cost: $', items_in_cart.show_cart(user))
                                            break
                                        
                                        
                                else:
                                    raise ValueError('Invalid, enter y/n')  
                            except ValueError as error:
                                    print(error) 
                        break
                    elif deposit == 'n':
                        print('You must agree to deposit agreement') 
                    else:                        
                        raise ValueError('Invalid, enter y/n')  
                except ValueError as error:
                        print(error) 
                        
        else:
            try:
                product_selection = int(product_selection)
                if 1 <= product_selection <= len(all_products):
                    selected_key = list(all_products.keys())[product_selection - 1]
                    selected_item = all_products[selected_key]
                    stock_quantity = selected_item.quantity
                    print(f'You selected: {selected_item.product_name}')
                    while True:
                        
                        rental_date = input('Enter the dates of rental (MM/DD/YYYY): ')
                        try:
                            #convert date to date datetime obj
                            rental_date = datetime.datetime.strptime(rental_date, "%m/%d/%Y").date()
                            if rental_date <= datetime.date.today():
                                print('Invalid, enter a future date')
                            elif not selected_item.available(rental_date):
                                print(f'{selected_item.product_name} is not available for rent on {rental_date.strftime("%m/%d/%Y")}')
                            else:
                                break
                        except ValueError:
                            print('Invalid Date: enter proper formart MM/DD/YYYY')
            
                    while True:
                        try:
                                # Try to get a valid float input
                                user_quantity_selection = float(input('Enter the quantity: '))
                                if user_quantity_selection > stock_quantity:
                                    print('We only have ', stock_quantity, ' left')
                                items_in_cart.add_to_cart(user, selected_item, selected_key, user_quantity_selection, rental_date)
                                selected_item.update_availability(rental_date, user_quantity_selection)

                                updated_stock_quantity, updated_user_quantity_selection = selected_item.update_quantity(stock_quantity, user_quantity_selection)
                                all_products[selected_key].quantity = updated_stock_quantity
                                all_products[selected_key].user_quantity = updated_user_quantity_selection
                    
                                break

                        except ValueError:
                                print(f'Unavailable, we have {stock_quantity} in stock. Enter a proper quantity.')
                else:
                    print('Invalid, choose a number within range')
                        
            except ValueError as e:
                print(f'Incorrect Value {e}')
                
        



if __name__ == "__main__":
    main()
 