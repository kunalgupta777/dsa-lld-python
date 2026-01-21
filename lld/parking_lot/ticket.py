from datetime import time
from lld.parking_lot.parking_spot import ParkingSpot
from lld.parking_lot.vehicle import Vehicle


class Ticket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot, entry_time: time, exit_time: time) -> None:
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = entry_time
        self.exit_time = exit_time
