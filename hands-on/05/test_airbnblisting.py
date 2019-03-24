import unittest
import csv
from datetime import date

from airbnblisting import AirbnbListing

class TestAirbnbListing(unittest.TestCase):

    listings = list()

    @classmethod
    def row_to_listing(cls, row):
        yyyy, mm, dd = row['last_review'].split('-') if row['last_review'] else ('1970', '1', '1')
        reviews_per_month = float(row['reviews_per_month']) if row['reviews_per_month'] else 0.0
        return AirbnbListing(
                id=int(row['id']),
                host_id=int(row['host_id']),
                neighbourhood_group=row['neighbourhood_group'],
                neighbourhood=row['neighbourhood'],
                minimum_nights=int(row['minimum_nights']),
                room_type=row['room_type'],
                price=int(row['price']),
                name=row['name'],
                host_name=row['host_name'],
                last_review=date(int(yyyy), int(mm), int(dd)),
                number_of_reviews=int(row['number_of_reviews']),
                reviews_per_month=reviews_per_month,
                calculated_host_listings_count=int(row['calculated_host_listings_count']),
                availability_365=int(row['availability_365']),
                lat_long=(float(row['latitude']), float(row['longitude'])))

    @classmethod
    def setUpClass(cls):
        filename = 'Airbnb Summary Listings NYC 2019-03-06.csv'
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                listing = TestAirbnbListing.row_to_listing(row)
                TestAirbnbListing.listings.append(listing)

    def test_repr(self):
        self.assertEqual(str(TestAirbnbListing.listings[-1]),'''AirbnbListing(id=32858895, host_id=8454981, '''
            '''neighbourhood_group='Manhattan', neighbourhood="Hell's Kitchen", minimum_nights=3, '''
            '''room_type='Entire home/apt', price=150, lat_long=(40.75711, -73.99796))''')

    def test_compare(self):
        listings = TestAirbnbListing.listings
        equivalent_listings = [l for l in listings if l == listings[-1]] # last listing and those equivalent to it
        self.assertEqual(len(equivalent_listings), 5)

    def test_lat_long(self):
        self.assertEqual(TestAirbnbListing.listings[200].lat_long, (40.8064, -73.92395))

    def test_long_stay(self):
        long_stay = [l for l in TestAirbnbListing.listings if l.requires_long_stay()]
        self.assertEqual(len(long_stay), 4903)

    def test_is_manhattan_long_stay(self):
        manhattan_long_stay = [l for l in TestAirbnbListing.listings if l.requires_long_stay() and l.is_manhattan()]
        self.assertEqual(len(manhattan_long_stay), 3239)

    def test_minimum_cost(self):
         self.assertEqual(TestAirbnbListing.listings[200].minimum_cost(), 165)

    def test_cost_for_stay(self):
         self.assertEqual(TestAirbnbListing.listings[300].cost_for_stay(5), None)
         self.assertEqual(TestAirbnbListing.listings[300].cost_for_stay(15), 1950)

if __name__ == '__main__':
    unittest.main()