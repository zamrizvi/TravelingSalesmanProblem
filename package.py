import csv
from hashTable import HashTable
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.deliveryTime = None
        self.departureTime = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.weight, self.deliveryTime)

"""
    def updateStatus(self, time):
        if self.deliveryTime < time:
            self.packageStatus = "Delivered"
        elif self.departureTime > time:
            self.packageStatus = "En Route"
        else:
            self.packageStatus = "At Hub"
            """

def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            packageId = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageWeight = package[6]



            pack = Package(packageId, packageAddress, packageCity, packageState, packageZip, packageDeadline,
                           packageWeight)

            myHash.insert(packageId, pack)



myHash = HashTable()

loadPackageData('WGUPS Package File.csv')



