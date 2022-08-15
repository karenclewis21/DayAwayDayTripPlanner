from secrets import choice
from tkinter.messagebox import NO


print('Welcome to Day Away Day Planner')
print('')
print('We can now get started planning your day!')
print('')
destinations = ['Gulf Shores', 'Huntsville', 'Nashville', 'Atlanta']
# print (destinations)
restaurants = ['Flemmings', 'Pappadeauxs','Surin', 'Jalapenos']
# print(restaurants)
entertainment = ['Ziplining Ride', 'Hot Air Balloon Ride', 'Horseback Ride', 'Shopping Spree']
# print(entertainment)
transportation = ['Train', 'Car', 'Plane', 'RV']
# print(transportation)



# while True:
    valid_response = False
    while valid_response == False:    
    
        rand_dest = choice(destinations)
        day_dest = input(f'\nIs {rand_dest} somewhere you would like to spend the day? Yes/No ') 

        if day_dest == "Yes":
                print ('\nThat is a beautful place to spend the day!')
                valid_response = True

        else:
                print('\nWe can try another destination.') 

    valid_response = False
    while valid_response == False:

        rand_trans = choice(transportation)
        day_trip_trans = input(f'\nWould {rand_trans} be a fun way to travel for the day?  Yes/No  ')

        if day_trip_trans == "Yes":
            print('\nThe only way to travel!')
            valid_response = True

        else:
            print('\nWe can get there another way.')

    valid_response = False
    while valid_response == False:

        rand_rest = choice(restaurants)

        day_trip_rest = input(f'\nDoes {rand_rest} sound like a good place to eat? Yes/ No ' )

        if day_trip_rest == "Yes":
            print('\nOhhh that sounds delicious!!')
            valid_response = True

        else:
            print('\nOk, we can choose another.')

    valid_response =False    
    while valid_response == False:
        
        rand_ent = choice(entertainment)

        day_trip_ent = input(f'\nHow would a {rand_ent} sound for the day? Yes/No ')

        if day_trip_ent == 'Yes':
            print('\nThat sounds so exciting!')
            valid_response = True

        else:
            print('\nWe can find another adventure for the day.')    

    day_trip_dictionary = {
    'destination' : rand_dest,
    'transportation'  : rand_trans,
    'restaurant'  : rand_rest,
    'entertainment' : rand_ent

    }

    print(f"\nYour trip will be to {rand_dest} and you will be traveling by {rand_trans}. There you will be enjoying a {rand_ent} and dining at {rand_rest}.")
    
    confirmation = input("\nAre you happy with your plans for the day? Yes/No  ")

    if confirmation == "Yes":
        print('\nHave an amazing Day Trip!!')
        valid_response = True
        break
    else:
        print('\nWe should try again then!')
        continue