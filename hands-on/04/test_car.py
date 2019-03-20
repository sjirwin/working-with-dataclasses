import unittest
from datetime import date

from car import Car

class TestCar(unittest.TestCase):

    def test_repr(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        self.assertEqual(str(car), "Car(make='BMW', model='i3', year=2019)")

    def test_compare(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        self.assertEqual(car, Car(make='BMW', model='i3', year=2019, price=42_000))

    def test_not_compare(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        self.assertNotEqual(car, Car(make='Chevrolet', model='Volt', year=2019, price=34_095))

    def test_price(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        self.assertEqual(car.price, 44_450)

    def test_no_oil_changes(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        self.assertEqual(car.oil_changes, [])

    def test_oil_changes(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        dt = date(2019,3,1)
        car.oil_changes.append(dt)
        self.assertEqual(car.oil_changes, [dt])

    def test_oil_changes_compare(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        car.oil_changes.append(date(2019,3,1))
        self.assertNotEqual(car.oil_changes, Car(make='BMW', model='i3', year=2019, price=44_450).oil_changes)

    def test_oil_changes_car_compare(self):
        car = Car(make='BMW', model='i3', year=2019, price=44_450)
        car.oil_changes.append(date(2019,3,1))
        self.assertEqual(car, Car(make='BMW', model='i3', year=2019, price=44_450))

if __name__ == '__main__':
    unittest.main()