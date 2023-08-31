#Zamir Rizvi
#ID: 010508494

import csv

def read_csv(file_path):
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

csv_file_path = 'WGUPS Package File.csv'
read_csv(csv_file_path)