from uuid import uuid4
from lld.parking_lot.parking_floor import ParkingFloor


class ParkingLot:
    def __init__(self, floors: list[ParkingFloor]) -> None:
        self.lot_id = uuid4()
        self.floors = floors
    
    def is_lot_full(self) -> bool:
        for floor in self.floors:
            if not floor.is_floor_full():
                return False
        
        return True
        