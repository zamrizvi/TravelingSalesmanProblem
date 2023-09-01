import csv
import datetime

#Read the csv files
#create a list of data to access later
with open('distances.csv') as distances:
    distanceData = csv.reader(distances, delimiter=',')
    distanceData = list(distanceData)
with open('addresses.csv') as addresses:
    addressData = csv.reader(addresses, delimiter=',')
    addressData = list(addressData)

#Calculate the distance
def calcDistance(row, column, total):
    distance = distanceData[row][column]
    if distance == '':
        distance = distanceData[column][row]

    return total + float(distance)

#calculate the distance between the current distance between two destinations
def calcCurrentDistance(row, column):
    distance = distanceData[row][column]
    if distance == '':
        distance = distanceData[column][row]

    return float(distance)

#get address from the address data list created earlier
def getAddress(address):
    for row in addressData:
        if address in row[2]:
            return int(row[0])



