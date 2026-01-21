from lld.parking_lot.entities.ticket import Ticket
from lld.parking_lot.pricing.pricing_strategies import DiscountedPricingStrategy, DefaultPricingStrategy, PricingStrategy


class StrategyResolver:
    def __init__(self, ticket: Ticket) -> None:
        self.ticket = ticket
    
    def get_pricing_strategy(self) -> PricingStrategy:
        exit_time = self.ticket.exit_time
        if exit_time.weekday() >= 5:
            print("Using Discounted Pricing Strategy")
            return DiscountedPricingStrategy(self.ticket)
        else:
            print("Using Default Pricing Strategy")
            return DefaultPricingStrategy(self.ticket)

