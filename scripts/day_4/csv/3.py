# Writing lists to csv file using csv.writer
import csv

with open('data2.csv', mode='w', newline='') as f:
    employee_writer = csv.writer(f, delimiter=',')

    employee_writer.writerow(['Jan Kowalski', 'HR', 'mar'])
    employee_writer.writerow(['Ewa Nowak', 'IT', 'lis'])
