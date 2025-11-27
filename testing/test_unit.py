import pytest
from datetime import date, timedelta
from source_code.rental_system import RentalSystem
from source_code.models import Vehicle

def test_vehicle_addition():
    system = RentalSystem()
    v = Vehicle("59A-12345", "Sedan", "Available", "Red Camry", 50.0)
    system.add_vehicle(v)
    assert len(system.vehicles) == 1
    assert system.vehicles[0].license_plate == "59A-12345"

def test_booking_logic():
    system = RentalSystem()
    v = Vehicle("59A-12345", "Sedan", "Available", "Red Camry", 50.0)
    system.add_vehicle(v)
    cust = system.register_customer(1, "User", "u@test.com", "pass")
    
    start = date.today()
    end = date.today() + timedelta(days=3)
    
    booking, cost = system.create_booking(cust, "59A-12345", start, end)
    
    assert booking is not None
    assert cost == 150.0 
    assert v.status == "Rented"