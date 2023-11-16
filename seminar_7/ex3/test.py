from ex3.statistic import Statistic
from ex3.car import Car

def test_average():
    cars = [Car('Mercedes', 'S-Class', 2023, 'black'),
            Car('Mercedes', 'S-Class', 2017, 'black'),
            Car('Skoda', 'Oktavia', 2014, 'grey')]

    stats = Statistic(cars)
    assert stats.average_year('S-Class') == 2020
