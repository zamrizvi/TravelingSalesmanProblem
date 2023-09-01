import csv
import datetime

class Truck:
    def __init__(self, location, departure, miles, packages):
        self.location = location
        self.departure = departure
        self.miles = miles
        self.packages = packages

    def __str__(self):
        return "%s, %s, %s, %s" %(self.location, self.departure, self.miles, self.packages)