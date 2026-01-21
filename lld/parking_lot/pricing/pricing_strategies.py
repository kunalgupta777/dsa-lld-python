from lld.parking_lot.entities.ticket import Ticket
from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_final_cost(self) -> float:
        pass

class DefaultPricingStrategy(PricingStrategy):
    def __init__(self, ticket: Ticket) -> None:
        self.ticket = ticket
        self.default_hourly_rate = 2.00
    
    def calculate_final_cost(self) -> float:
        if not self.ticket.exit_time:
            raise ValueError("Vehicle hasn't vacated the parking spot yet!")

        if self.ticket.parking_spot.hourly_rate:
            hourly_rate = self.ticket.parking_spot.hourly_rate
        else:
            hourly_rate = self.default_hourly_rate
        
        time_elapsed = self.ticket.exit_time - self.ticket.entry_time
        return hourly_rate * time_elapsed.total_seconds()/3600

class DiscountedPricingStrategy(PricingStrategy):
    def __init__(self, ticket: Ticket) -> None:
        self.ticket = ticket
        self.default_hourly_rate = 1.75
        self.discount_factor = 0.97

    def calculate_final_cost(self) -> float:
        if not self.ticket.exit_time:
            raise ValueError("Vehicle hasn't vacated the parking spot yet!")

        if self.ticket.parking_spot.hourly_rate:
            hourly_rate = self.ticket.parking_spot.hourly_rate
        else:
            hourly_rate = self.default_hourly_rate
        
        time_elapsed = self.ticket.exit_time - self.ticket.entry_time
        return self.discount_factor * hourly_rate * time_elapsed.total_seconds()/3600
        
        