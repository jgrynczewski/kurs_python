# Reading csv file using csv.reader
import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        print(row)



