from datetime import date

class Vehicle:
    def __init__(self, license_plate, vehicle_type, status, details, price_per_day):
        self.license_plate = license_plate 
        self.vehicle_type = vehicle_type
        self.status = status
        self.details = details
        self.price_per_day = price_per_day

    def update_status(self, new_status):
        self.status = new_status

    def update_details(self, new_details):
        self.details = new_details

class Customer:
    def __init__(self, customer_id, name, email, password):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password
        self.login_info = f"{email}:{password}"

    def verify_login(self, email, password):
        return self.email == email and self.password == password

class Booking:
    def __init__(self, booking_id, customer, vehicle, start_date, end_date):
        self.booking_id = booking_id
        self.customer = customer
        self.vehicle = vehicle
        self.booking_date = date.today()
        self.pickup_date = start_date
        self.return_date = end_date
        self.booking_status = "Confirmed"

    def calculate_rental_days(self):
        delta = self.return_date - self.pickup_date
        return delta.days

    def confirm_booking(self):
        self.booking_status = "Active"
        self.vehicle.update_status("Rented")

class Payment:
    def __init__(self, payment_id, amount, method):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_date = date.today()
        self.method = method
        self.status = "Completed"

    def process_payment(self):
        print(f"Processing payment of ${self.amount} via {self.method}")
        return True