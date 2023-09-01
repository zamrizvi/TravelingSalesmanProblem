import csv
import datetime

with open('distances.csv') as distances:
    distanceData = csv.reader(distances, delimiter=',')
    distanceData = list(distanceData)
with open('addresses.csv') as addresses:
    addressData = csv.reader(addresses, delimiter=',')
    addressData = list(addressData)


def calcDistance(row, column, total):
    distance = distanceData[row][column]
    if distance == '':
        distance = distanceData[column][row]

    return total + float(distance)

def calcCurrentDistance(row, column):
    distance = distanceData[row][column]
    if distance == '':
        distance = distanceData[column][row]

    return float(distance)

def getAddress(address):
    for row in addressData:
        if address in row[2]:
            return int(row[0])



