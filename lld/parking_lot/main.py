

from uuid import uuid4
from lld.parking_lot import vehicle
from lld.parking_lot.parking_floor import ParkingFloor
from lld.parking_lot.parking_handler import ParkingHandler
from lld.parking_lot.parking_lot import ParkingLot
from lld.parking_lot.parking_spot import ParkingSpot
from lld.parking_lot.vehicle import Vehicle, VehicleType

import random

def create_parking_spots(num = 100) -> list[ParkingSpot]:
    spots = []
    hourly_rates = [2, 3, 4, 5, 7, 10]
    for i in range(num):
        spots.append(ParkingSpot(hourly_rate=random.choice(hourly_rates), vehicle_types=[VehicleType.TWO_WHEELER, VehicleType.THREE_WHEELER, VehicleType.FOUR_WHEELER]))
    return spots

def create_parking_floors(levels = 5) -> list[ParkingFloor]:
    floors = []
    for i in range(levels):
        spots = create_parking_spots()
        floor = ParkingFloor(spots=spots, floor_level=i+1)
        floors.append(floor)
    
    return floors

def create_vehicles(count = 501):
    vehicles = []
    vehicle_types = [VehicleType.TWO_WHEELER, VehicleType.THREE_WHEELER, VehicleType.FOUR_WHEELER]
    for i in range(count):
        vehicles.append(Vehicle(type=random.choice(vehicle_types), license_number=str(uuid4())))
    return vehicles

if __name__ == "__main__":
    parking_lot = ParkingLot(floors=create_parking_floors())
    parking_handler = ParkingHandler(parking_lot=parking_lot)
    vehicles = create_vehicles()
    for id, vehicle in enumerate(vehicles):
        try: 
            ticket = parking_handler.park_vehicle(vehicle=vehicle)
            print(str(id) + " Ticket received!", ticket.__dict__)
        except Exception as e:
            print("Some error occured while parking this vehicle!", e)




