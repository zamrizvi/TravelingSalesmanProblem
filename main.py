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
        nextPackage.deliveryTime = truck.departure
        nextPackage.departureTime = truck.departure

deliveryAlgorithm(truckOne)
deliveryAlgorithm(truckTwo)

truckThree.departure = min(truckOne.departure, truckTwo.departure)
deliveryAlgorithm(truckThree)




class Main:
    print("WGUPS Package Tracker")
    print("---------------------")

    print("Total Milage: {:.2f} miles".format(truckOne.miles + truckTwo.miles + truckThree.miles))

    userTimeOne = input("Enter time 1:")
    (h1, m1, s1) = userTimeOne.split(":")
    userTimeTwo = input("Enter time 2:")
    (h2, m2, s2) = userTimeTwo.split(":")
    convertUserTimeOne = datetime.timedelta(hours=int(h1), minutes=int(m1), seconds=int(s1))
    convertUserTimeTwo = datetime.timedelta(hours=int(h2), minutes=int(m2), seconds=int(s2))


    for id in range(1, 41):
        package = myHash.search(id)
        if package.deliveryTime < convertUserTimeOne:
            print(str(package))
            print("Delivered")
        elif package.deliveryTime > convertUserTimeOne and package.deliveryTime < convertUserTimeTwo:
            print(str(package))
            print("En Route")
        else:
            print(str(package))
            print("At Hub")


