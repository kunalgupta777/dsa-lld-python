from lld.parking_lot import parking_spot
from lld.parking_lot import payment_processor
from lld.parking_lot.parking_floor import ParkingFloor
from lld.parking_lot.parking_lot import ParkingLot
from lld.parking_lot.parking_spot import ParkingSpot
from lld.parking_lot.payment_processor import PaymentProcessor
from lld.parking_lot.ticket import Ticket
from lld.parking_lot.vehicle import Vehicle

import datetime


class ParkingHandler:
    def __init__(self, parking_lot: ParkingLot) -> None:
        self.parking_lot = parking_lot 
        self.floors = { floor.floor_level: floor for floor in self.parking_lot.floors }
        self.parking_spot_to_vehicle = {}
        self.vehicle_to_parking_spot = {}
        self.license_number_to_vehicle = {}
        self.spot_id_to_parking_spot = {}
        for floor in self.parking_lot.floors:
            for spot in floor.spots:
                self.spot_id_to_parking_spot[spot.spot_id] = spot

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        self.license_number_to_vehicle[vehicle.license_number] = vehicle
        if self.parking_lot.is_lot_full():
            raise Exception("Sorry, parking lot is full!")
        try:
            parking_spot_assigned = self._find_nearest_vacant_spot(vehicle)
        except Exception as e:
            raise Exception("Cannot find any valid spot!", e)
        parking_spot_assigned.is_spot_vacant = False
        ticket = Ticket(vehicle, parking_spot_assigned, datetime.datetime.now(), None)
        self.parking_spot_to_vehicle[parking_spot_assigned.spot_id] = vehicle.license_number
        self.vehicle_to_parking_spot[vehicle.license_number] = parking_spot_assigned.spot_id
        print("Vehicle Parked successfully at spot:", str(parking_spot_assigned.spot_id))
        return ticket
        

    def unpark_vehicle(self, ticket: Ticket) -> None:
        if not ticket:
            raise ValueError("Invalid ticket!")

        ticket.exit_time = datetime.datetime.now()
        vehicle = ticket.vehicle
        parking_spot = ticket.parking_spot
        payment_processor = PaymentProcessor(ticket)
        final_cost = payment_processor.calculate_final_cost()
        print("Total cost for the vehicle's parking is " + str(final_cost * 1e8) + " USD.")
        ## Integrate with a payments engine like Stripe to get the final payment
        parking_spot.is_spot_vacant = True 
        del self.parking_spot_to_vehicle[parking_spot.spot_id]
        del self.vehicle_to_parking_spot[vehicle.license_number]
        print("Vehicle unparked!")

    
    def _find_nearest_vacant_spot(self, vehicle: Vehicle) -> ParkingSpot:
        for floor_level in sorted(list(self.floors.keys())):
            floor = self.floors[floor_level]
            if not floor.is_floor_full():
                parking_spot = self._get_vacant_spot_on_floor(floor, vehicle)
                if parking_spot:
                    return parking_spot
        raise Exception("No Valid Parking spot found!")
    
    def _get_vacant_spot_on_floor(self, floor: ParkingFloor,  vehicle: Vehicle) -> ParkingSpot:
        for spot in floor.spots:
            if spot.is_spot_vacant and vehicle.vehicle_type in spot.vehicle_types:
                return spot
        
        return None
    
    def find_parking_spot_from_license_number(self, license_number: str) -> ParkingSpot:
        if license_number not in self.vehicle_to_parking_spot.keys():
            raise Exception("Sorry we don't have any data for this vehicle!")
        spot_id = self.vehicle_to_parking_spot[license_number]
        if spot_id not in self.spot_id_to_parking_spot.keys():
            raise Exception("We cannot find relevant parking spot for this ID!")
        return self.spot_id_to_parking_spot[spot_id]
    
    def get_total_vacant_spots(self) -> int:
        vacant_spots = 0
        for floor in self.parking_lot.floors:
            for spot in floor.spots:
                if spot.is_spot_vacant:
                    vacant_spots += 1
        return vacant_spots