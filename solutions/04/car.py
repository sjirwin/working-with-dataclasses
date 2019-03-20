from dataclasses import dataclass, field
from datetime import date
from typing import List

# TODO: finish implementing Car.
#       fields to be added
#           price : int. exclude from compare and exclude from repr
#           oil_changes : list of date. exclude from compare and exclude from repr
@dataclass
class Car:
    make: str
    model: str
    year: int
    price: int = field(compare=False, repr=False)
    oil_changes: List[date] = field(default_factory=list, compare=False, repr=False)
