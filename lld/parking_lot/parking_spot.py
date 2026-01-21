from uuid import uuid4

from lld.parking_lot.vehicle import VehicleType

class ParkingSpot:
    def __init__(self, hourly_rate: float, vehicle_types: list[VehicleType]) -> None:
        self.spot_id = uuid4()
        self.hourly_rate = hourly_rate
        self.is_spot_vacant = True
        self.vehicle_types = vehicle_types