from models import Vehicle, Customer, Booking, Payment
from datetime import date

class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        self.bookings = []
        self.next_booking_id = 1

    def register_customer(self, customer_id, name, email, password):
        new_customer = Customer(customer_id, name, email, password)
        self.customers.append(new_customer)
        return new_customer

    def login(self, email, password):
        for cust in self.customers:
            if cust.verify_login(email, password):
                return cust
        return None

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def search_vehicles(self, vehicle_type=None):
        results = []
        for v in self.vehicles:
            if v.status == "Available":
                if vehicle_type is None or v.vehicle_type == vehicle_type:
                    results.append(v)
        return results

    def create_booking(self, customer, license_plate, start_date, end_date):
        vehicle = next((v for v in self.vehicles if v.license_plate == license_plate), None)
        
        if vehicle and vehicle.status == "Available":
            new_booking = Booking(self.next_booking_id, customer, vehicle, start_date, end_date)
            days = new_booking.calculate_rental_days()
            
            total_cost = days * vehicle.price_per_day
            
            self.bookings.append(new_booking)
            self.next_booking_id += 1
            
            vehicle.update_status("Rented")
            
            return new_booking, total_cost
        return None, 0