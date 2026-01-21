

from uuid import uuid4
from lld.parking_lot.entities.parking_floor import ParkingFloor
from lld.parking_lot.parking_service import ParkingService
from lld.parking_lot.entities.parking_lot import ParkingLot
from lld.parking_lot.entities.parking_spot import ParkingSpot
from lld.parking_lot.entities.vehicle import Vehicle, VehicleType

import random

vehicle_types = [VehicleType.TWO_WHEELER, VehicleType.THREE_WHEELER, VehicleType.FOUR_WHEELER]

def create_parking_spots(num = 10) -> list[ParkingSpot]:
    spots = []
    hourly_rates = [2, 3, 4, 5, 7, 10]
    for i in range(num):
        spots.append(ParkingSpot(hourly_rate=random.choice(hourly_rates), vehicle_types=random.choices(vehicle_types)))
    return spots

def create_parking_floors(levels = 5) -> list[ParkingFloor]:
    floors = []
    for i in range(levels):
        spots = create_parking_spots()
        floor = ParkingFloor(spots=spots, floor_level=i+1)
        floors.append(floor)
    
    return floors

def create_vehicles(count = 51) -> list[Vehicle]:
    vehicles = []
    for i in range(count):
        vehicles.append(Vehicle(type=random.choice(vehicle_types), license_number=str(uuid4())))
    return vehicles

if __name__ == "__main__":
    parking_lot = ParkingLot(floors=create_parking_floors())
    parking_service = ParkingService(parking_lot=parking_lot)
    vehicles = create_vehicles()
    tickets = []
    for id, vehicle in enumerate(vehicles):
        print("#" + str(id+1) + ": Attempting to park vehicle:" + vehicle.license_number)
        try: 
            ticket = parking_service.park_vehicle(vehicle=vehicle)
            tickets.append(ticket)
            # print(str(id) + " Ticket received!", ticket.__dict__)
        except Exception as e:
            print("Some error occured while parking this vehicle!", e)
        print("Total vacant spots:" + str(parking_service.get_total_vacant_spots()))
    
    for ticket in tickets:
        vehicle = ticket.vehicle
        spot = parking_service.find_parking_spot_from_license_number(vehicle.license_number)
        print("Vehicle " + vehicle.license_number + " is parked at: " + str(spot.spot_id))
        print("#" + str(id+1) + ": Attempting to unpark vehicle:" + ticket.vehicle.license_number)
        try:
            parking_service.unpark_vehicle(ticket=ticket)
        except Exception as e:
            print("Error unparking vehicle!", e)
        print("Total vacant spots:" + str(parking_service.get_total_vacant_spots()))






