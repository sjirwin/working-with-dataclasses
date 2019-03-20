import unittest

import dataclasses
from airbnblisting import AirbnbListing

_listing = AirbnbListing(id=2539, host_id=2787, latitude=40.64749, longitude=-73.97237)

class TestAirbnbListing(unittest.TestCase):
    
    def test_getattr(self):
        self.assertEqual(_listing.id, 2539)
        self.assertEqual(_listing.host_id, 2787)

    def test_setattr(self):
        with self.assertRaises(dataclasses.FrozenInstanceError):
            _listing.latitude = 39.8

if __name__ == '__main__':
    unittest.main()