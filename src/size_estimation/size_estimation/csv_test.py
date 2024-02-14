# Author: Enrico Mendez
# Date: 14 Febrero 2024
# Description: Csv manager test

import csv

file_name = 'test.csv'

header = ['Nombre', 'Edad', 'Ciudad']
content = [
    ['Ana', 25, 'Querétaro'],
    ['Carlos', 30, 'Ciudad de México']
]

def reader_csv(file_name):
    with open (file_name, 'r') as my_file:
        writer = csv.writer(my_file)

        writer.writerow(content[0])

def create_csv(file_name):
    with open (file_name, 'x') as my_file :
        writer = csv.writer(my_file)

        writer.writerow(header)

try: 
    reader_csv(file_name)
    print('File successfully read')
except: 
    create_csv(file_name)
    print('File couldn\'t be read, a new file {} was created'.format(file_name))
