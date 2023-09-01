#Zamir Rizvi
#ID: 010508494

import csv
from package import Package
from package import myHash

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
"""

#printing out packages from hashtable
print("packages from hash table")

for i in range(len(myHash.table) + 1):
    print("Packages: {}".format(myHash.search(i + 1)))

