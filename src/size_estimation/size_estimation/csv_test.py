# Author: Enrico Mendez
# Date: 14 Febrero 2024
# Description: Csv manager test

import csv
import os
from ament_index_python.packages import get_package_share_directory

pkg_path = get_package_share_directory('size_estimation')
print(pkg_path)
path = os.path.dirname(pkg_path)
print("Package source directory:", path)
parts = pkg_path.split('/')
print(parts)

replace = 'install'
idx = parts.index(replace)
parts[idx] = 'src'

# replace = 'share'
# idx = parts.index(replace)
# parts[idx] = ''
parts.remove('share')

print(parts)

parts = '/'.join(parts)
print(parts)

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

def main():
    try: 
        reader_csv(file_name)
        print('File successfully read')
    except: 
        create_csv(file_name)
        print('File couldn\'t be read, a new file {} was created'.format(file_name))
