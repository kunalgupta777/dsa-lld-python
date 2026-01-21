from uuid import uuid4
from lld.parking_lot.entities.parking_spot import ParkingSpot
from lld.parking_lot.entities.vehicle import Vehicle


class ParkingFloor:
    def __init__(self, spots: list[ParkingSpot], floor_level: int) -> None:
        self.floor_id = uuid4()
        self.spots = spots
        self.floor_level = floor_level
    
    def is_floor_full(self):
        for spot in self.spots:
            if spot.is_spot_vacant:
                return False
        return True
    
