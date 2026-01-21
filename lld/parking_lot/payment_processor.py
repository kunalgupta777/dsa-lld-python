from lld.parking_lot.ticket import Ticket


class PaymentProcessor:
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
        
        