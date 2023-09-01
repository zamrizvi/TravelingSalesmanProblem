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



#Created three tucks objects based on how many trucks available.
#With there being only 2 drivers, the third truck will have to leave after the one of the trucks returns to the hub
#Manually loaded the packages into each truck based on the constraints.
#TruckOne will have the packages that need to be delivered early
#TruckTwo will have packages that come to the hub later
#TruckThree will have packages that do not have strict constraints.
truckOne = truck.Truck("4001 South 700 East", datetime.timedelta(hours=8), 0.0,
                     [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])

truckTwo = truck.Truck("4001 South 700 East", datetime.timedelta(hours=9, minutes=5), 0.0,
                       [3, 6, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39])

truckThree = truck.Truck("4001 South 700 East", datetime.timedelta(hours=11), 0.0,
                         [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26])


#Using the "Nearest Neighbor" algorithm to deliver packages.
def deliveryAlgorithm(truck):
    #Create a list to store the packages in the optimal order
    setupPackages = []
    for packageId in truck.packages:
        package = myHash.search(packageId)
        setupPackages.append(package)

    #clear the packages that were in the truck so they can be put back in optimal order
    truck.packages.clear()

    #Loop through the packages so that the next package that is to be delivered is to
    #be delivered at the shortest next destination
    while len(setupPackages) > 0:
        nextAddress = 2000
        nextPackage = None
        for package in setupPackages:
            if calcCurrentDistance(getAddress(truck.location), getAddress(package.address)) <= nextAddress:
                nextAddress = calcCurrentDistance(getAddress(truck.location), getAddress(package.address))
                nextPackage = package


        setupPackages.remove(nextPackage)
        #calculates the milage the truck drove
        truck.miles += nextAddress
        #the next location the truck has to go is the next address
        truck.location = nextPackage.address
        #create a timestamp
        truck.departure += datetime.timedelta(hours=nextAddress / 18)
        #the delivery time of the current package is the same as when the truck departs to the next address
        nextPackage.deliveryTime = truck.departure
        #the departure time for the next package is the same as truck departure time
        nextPackage.departureTime = truck.departure

deliveryAlgorithm(truckOne)
deliveryAlgorithm(truckTwo)

truckThree.departure = min(truckOne.departure, truckTwo.departure)
deliveryAlgorithm(truckThree)




class Main:
    #Created a UI to have user enter two time to create a time block
    #Display the tracking information of the packages
    print("WGUPS Package Tracker")
    print("---------------------")

    print("Total Milage: {:.2f} miles".format(truckOne.miles + truckTwo.miles + truckThree.miles))

    userTimeOne = input("Enter time 1:")
    (h1, m1, s1) = userTimeOne.split(":")
    userTimeTwo = input("Enter time 2:")
    (h2, m2, s2) = userTimeTwo.split(":")
    convertUserTimeOne = datetime.timedelta(hours=int(h1), minutes=int(m1), seconds=int(s1))
    convertUserTimeTwo = datetime.timedelta(hours=int(h2), minutes=int(m2), seconds=int(s2))


    #Display the status of packages based on the package time and the time block the user entered
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


