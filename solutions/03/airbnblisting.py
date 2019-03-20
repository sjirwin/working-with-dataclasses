from dataclasses import dataclass

# TODO: add decorator option and fields
@dataclass(frozen=True)
class AirbnbListing:
    id: int
    host_id: int
    latitude: float
    longitude: float