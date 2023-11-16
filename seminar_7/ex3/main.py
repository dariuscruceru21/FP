from ex3.car import Car
from ex3.statistic import Statistic
from ex3.test import test_average



test_average()

def main():
    cars = [Car('Mercedes', 'C-Class', 2023, 'black'),
            Car('Mercedes', 'C-Class', 2023, 'black'),
            Car('Skoda', 'C-Class', 2023, 'grey')]

    stats = Statistic(cars)
    print(stats.color_count('black'),  stats.average_year('C-Class'))

main()
