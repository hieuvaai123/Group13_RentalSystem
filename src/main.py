import sys
from datetime import date, timedelta
from rental_system import RentalSystem
from models import Vehicle

def print_header():
    print("\n" + "="*40)
    print("      VEHICLE RENTAL SYSTEM")
    print("="*40)

def populate_dummy_data(system):
    v1 = Vehicle("59A-12345", "Sedan", "Available", "Toyota Camry - Red", 50.0)
    v2 = Vehicle("59B-67890", "SUV", "Available", "Honda CR-V - Black", 85.0)
    v3 = Vehicle("51F-99999", "Luxury", "Maintenance", "Mercedes S450", 200.0)
    
    system.add_vehicle(v1)
    system.add_vehicle(v2)
    system.add_vehicle(v3)
    
    system.register_customer(101, "Student Tester", "student01", "123456")

def customer_menu(system, current_user):
    while True:
        print(f"\n--- Welcome, {current_user.name} ---")
        print("1. Search Vehicles")
        print("2. Book a Vehicle")
        print("3. Logout")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            v_type = input("Enter vehicle type (Sedan/SUV) or press Enter for all: ").strip()
            v_type = v_type if v_type else None
            results = system.search_vehicles(v_type)
            
            print(f"\nFound {len(results)} available vehicle(s):")
            for v in results:
                print(f" - [{v.license_plate}] {v.vehicle_type}: {v.details} (${v.price_per_day}/day)")
                
        elif choice == '2':
            plate = input("Enter License Plate to book: ")
            try:
                days = int(input("How many days do you want to rent? "))
                start_date = date.today()
                end_date = start_date + timedelta(days=days)
                
                booking, cost = system.create_booking(current_user, plate, start_date, end_date)
                
                if booking:
                    print("\n--- BOOKING SUCCESSFUL ---")
                    print(f"Booking ID: {booking.booking_id}")
                    print(f"Vehicle: {booking.vehicle.details}")
                    print(f"Total Cost: ${cost} (Payment Processed via Credit Card)")
                else:
                    print("\nError: Vehicle not found or unavailable.")
            except ValueError:
                print("Invalid input for days.")

        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid option.")

def main():
    system = RentalSystem()
    populate_dummy_data(system)
    
    while True:
        print_header()
        print("1. Login")
        print("2. Register New Account")
        print("3. Exit")
        
        option = input("Choose an option: ")
        
        if option == '1':
            email = input("Email/Username: ")
            password = input("Password: ")
            user = system.login(email, password)
            
            if user:
                customer_menu(system, user)
            else:
                print("\n[!] Invalid credentials. Please try again.")
                
        elif option == '2':
            print("\n--- Create New Account ---")
            name = input("Full Name: ")
            email = input("Email/Username: ")
            password = input("Password: ")
            
            new_id = len(system.customers) + 101
            system.register_customer(new_id, name, email, password)
            print("\n[+] Account created! Please login.")
            
        elif option == '3':
            print("Exiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()