# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import os
import pickle
import Gjennomsnittsmåling

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
CHECK_SPEEDINGS = 6
QUIT_CHOICE = 7

DATA = "vehicles.data"

FILE_A = "box_a.txt"
FILE_B = "box_b.txt"
SPEED_LIMIT = 60
DISTANCE = 5

def main():
    # Create empty list for vehicles
    vehicles_list = []

    if os.path.isfile(DATA):
        with open(DATA, "rb") as f:
            try:
                vehicles_list = pickle.load(f)
            except:
                pass

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        try:
            choice = int(input('Enter your choice: '))
        except:
            print('Error: invalid selection.') 
            continue
        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('\nInput car data:')
            vehicles_list.append(vehicles.Car(
                input("Make: "),
                input("Year: "),
                input("Milage: "),
                input("Price: "),
                input("Registration number: "),
                input("Doors: "),
            ))
        elif choice == NEW_TRUCK_CHOICE:
            print('\nInput truck data:')
            vehicles_list.append(vehicles.Truck(
                input("Make: "),
                input("Year: "),
                input("Milage: "),
                input("Price: "),
                input("Registration number: "),
                input("Drivetype: "),
            ))
        elif choice == NEW_SUV_CHOICE:
            print('\nInput SUV data:')
            vehicles_list.append(vehicles.SUV(
                input("Make: "),
                input("Year: "),
                input("Milage: "),
                input("Price: "),
                input("Registration number: "),
                input("Number of passengers: "),
            ))
        elif choice == FIND_VEHICLE_CHOICE:
            make = input("\nEnter the name of your vehicle: ")
            found_one = False
            for vehicle in vehicles_list:
                if make in vehicle.get_make():
                    found_one = True
                    print(vehicle)
            if not found_one:
                print("Could not find your vehicle.")

        elif choice == CHECK_SPEEDINGS:
            speedings = Gjennomsnittsmåling.list_speeders(FILE_A, FILE_B, SPEED_LIMIT, DISTANCE)
            for vehicle in vehicles_list:
                reg_nr = vehicle.get_reg_nr()
                if reg_nr in speedings:
                    speed, timestamp = speedings[reg_nr]
                    new_ticket = Gjennomsnittsmåling.SpeedTicket(reg_nr, timestamp, speed, SPEED_LIMIT)
                    if new_ticket not in vehicle.get_all_tickets():
                        print("---new ticket---")
                        print(new_ticket)
                        vehicle.add_ticket(new_ticket)


        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            if len(vehicles_list) == 0:
                print("No vehicles found")

            for item in vehicles_list:
                print(item)
                if len(item.get_all_tickets()) > 0:
                    item.print_tickets()

        elif choice == QUIT_CHOICE:
            with open(DATA, "wb") as f:
                vehicles_list.sort(key=lambda x: x.get_make())
                pickle.dump(vehicles_list, f)

            print('Exiting the program...')    
        else:
            print('Error: invalid selection.')    

# The display_menu function displays a menu.
def display_menu():
    print('\n        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Check speedings')
    print('7) Quit')     

# Call the main function.
if __name__ == '__main__':
      main()