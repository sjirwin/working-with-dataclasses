from dataclasses import dataclass, field
from typing import Tuple
from datetime import date

# TODO: add the fields for an Airbnb listing. 
#       the field lat_long should be a tuple of two floats
#       the following fields should be included in repr:
#           id, host_id, neighbourhood_group, neighbourhood, neighbourhood, room_type, price, lat_long
#       the following fields should be included in compare:
#           neighbourhood_group, neighbourhood, neighbourhood, room_type, price
@dataclass
class AirbnbListing:
    id: int = field(compare=False)
    host_id: int = field(compare=False)
    neighbourhood_group: str
    neighbourhood: str
    minimum_nights: int
    room_type: str
    price: int
    name: str = field(compare=False, repr=False)
    host_name: str = field(compare=False, repr=False)
    last_review: date = field(compare=False, repr=False)
    number_of_reviews: int = field(compare=False, repr=False, default=0)
    reviews_per_month: float = field(compare=False, repr=False, default=0.0)
    calculated_host_listings_count: int = field(compare=False, repr=False, default=0)
    availability_365: int = field(compare=False, repr=False, default=0)
    lat_long: Tuple[float,float] = field(compare=False, default_factory=tuple)

    # TODO: implement is_manhattan()
    def is_manhattan(self):
        return self.neighbourhood_group == 'Manhattan'

    # TODO: implement requires_long_stay()
    def requires_long_stay(self):
        return self.minimum_nights >= 30

    # TODO: implement minimum_cost(). this the total cost of a minimum length stay 
    def minimum_cost(self):
        return self.price * self.minimum_nights

    # TODO: implement cost_for_stay(). this the total cost of the number of nights specified
    #       return None if nights is less than the minimum number of nights
    def cost_for_stay(self, nights):
        return self.price * nights if nights >= self.minimum_nights else None