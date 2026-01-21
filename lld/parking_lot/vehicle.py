from enum import Enum

class VehicleType(Enum):
    TWO_WHEELER = 1
    THREE_WHEELER = 2
    FOUR_WHEELER = 3

class Vehicle:
    def __init__(self, type: VehicleType, license_number: str) -> None:
        self.vehicle_type = type
        self.license_number = license_number
        

