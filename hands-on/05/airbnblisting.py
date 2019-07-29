from dataclasses import dataclass, field
from typing import Tuple
from datetime import date

# TODO: add the fields for an Airbnb listing. 
#       the field lat_long should be a tuple of two floats
#       the following fields should be included in repr:
#           id, host_id, neighbourhood_group, neighbourhood, minimum_nights, room_type, price, lat_long
#       the following fields should be included in compare:
#           neighbourhood_group, neighbourhood, minimum_nights, room_type, price
@dataclass
class AirbnbListing:

    # TODO: use neighbourhood_group to implement is_manhattan()
    #       values for neighbourhood_group are Bronx, Brooklyn, Manhattan, Queens, Staten Island
    def is_manhattan(self):
        pass

    # TODO: implement requires_long_stay(). A long stay is defined as minimum_nights >= 30
    def requires_long_stay(self):
        pass

    # TODO: implement minimum_cost(). this the total cost of a minimum length stay 
    def minimum_cost(self):
        pass

    # TODO: implement cost_for_stay(). this the total cost of the number of nights specified
    #       return None if nights is less than the minimum number of nights
    def cost_for_stay(self, nights):
        pass
