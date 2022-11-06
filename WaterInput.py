""""
asks user for the aount of times they performed
certain event and tracks the amount of times perform
each task 

stores the count of each task in a text file 

"""

with open('water.txt', 'w+') as f:

    bath_count = 0
    drink = 0
    shower = 0
    wHands = 0
    dWash = 0
    laundry = 0
    garden = 0

    print("Welcome to the Water Tracking Program!")
    begin_input = int(input("1 for Bathroom\n2 for Drinking Water\n3 for Shower\n4 for Wash Hands\n5 for Dish Washing\n6 Laundry\n7 for Gardening\n8 to quit\n"))

    while begin_input != 8:
        if begin_input == 1:
            bath_count += 1
            print("You used the restroom")
        elif begin_input == 2:
            drink += 1
            print("You drank one bottle of water")
        elif  begin_input == 3:
            shower += 1
            print("You showered")
        elif begin_input == 4:
            wHands += 1
            print("You washed your hands")
        elif begin_input == 5:
            dWash += 1
            print("You washed the dishes")
        elif begin_input == 6:
            laundry += 1
            print("You did laundry")
        elif begin_input == 7:
            garden += 1
            print("You gardened")
        begin_input = int(input())
        
        


    f.write(f'bathroom {bath_count}\n')
    f.write(f'drink {drink}\n')
    f.write(f'shower {shower}\n')
    f.write(f'sink {wHands}\n')
    f.write(f'dishes {dWash}\n')
    f.write(f'gardening {garden}\n')
    f.write(f'laundry {laundry}\n')
    

    f.close()