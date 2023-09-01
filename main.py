#Zamir Rizvi
#ID: 010508494

import csv
import datetime

from package import myHash
import truck
from distances import calcDistance
from distances import calcCurrentDistance
from distances import getAddress
from package import Package

"""
#printing out csv data to make sure it looks good
def read_csv(file_path):
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

csv_file_path = 'WGUPS Package File.csv'
csv_file_two = 'addresses.csv'
csv_file_three = 'distances.csv'
read_csv(csv_file_path)
read_csv(csv_file_two)
read_csv(csv_file_three)


#printing out packages from hashtable
print("packages from hash table")

for i in range(len(myHash.table) + 1):
    print("Packages: {}".format(myHash.search(i + 1)))
    """

truckOne = truck.Truck("4001 South 700 East", datetime.timedelta(hours=8), 0.0,
                     [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])

truckTwo = truck.Truck("4001 South 700 East", datetime.timedelta(hours=9, minutes=5), 0.0,
                       [3, 6, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39])

truckThree = truck.Truck("4001 South 700 East", datetime.timedelta(hours=11), 0.0,
                         [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26])


def deliveryAlgorithm(truck):
    setupPackages = []
    for packageId in truck.packages:
        package = myHash.search(packageId)
        setupPackages.append(package)

    truck.packages.clear()

    while len(setupPackages) > 0:
        nextAddress = 2000
        nextPackage = None
        for package in setupPackages:
            if calcCurrentDistance(getAddress(truck.location), getAddress(package.address)) <= nextAddress:
                nextAddress = calcCurrentDistance(getAddress(truck.location), getAddress(package.address))
                nextPackage = package

        #truck.packages.append(nextPackage.packageId)
        setupPackages.remove(nextPackage)
        truck.miles += nextAddress
        truck.location = nextPackage.address
        truck.departure += datetime.timedelta(hours=nextAddress / 18)

deliveryAlgorithm(truckOne)
deliveryAlgorithm(truckTwo)

truckThree.departure = min(truckOne.departure, truckTwo.departure)
deliveryAlgorithm(truckThree)

print(truckOne.miles + truckTwo.miles + truckThree.miles)


"""
def greedyAlgorithm(packageList, truckNumber, currentlocation):
    if len(packageList) == 0:
        return packageList

    lowestValue = 50.0
    location = 0

    for i in packageList:
        value = int(i[1])
        if calcCurrentDistance(currentlocation, value) <= lowestValue:
            lowestValue = calcCurrentDistance(currentlocation, value)
            location = value

    for i in packageList:
        if calcCurrentDistance(currentlocation, int(i[1])) == lowestValue:
            if truckNumber == 1:
                truckOne.append(i)
"""

