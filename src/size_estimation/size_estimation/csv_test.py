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
parts.remove('share')

print(parts)

parts = '/'.join(parts)
print(parts)
os.system('cd {}'.format(parts))

file_name = 'test.csv'

header = ['id', 'Nombre', 'Edad', 'Ciudad']
content = [
    [1, 'Ana', 25, 'Querétaro'],
    [2, 'Carlos', 30, 'Ciudad de México'],
    [3, 'Ana', 25, 'Querétaro'],
    [4, 'Ana', 25, 'Querétaro']
]

def reader_csv(file_name):
    with open (file_name, 'r+') as my_file:
        text_read = csv.reader(my_file)
        data = list(text_read)
    return data

def create_csv(file_name):
    with open (file_name, 'x') as my_file :
        writer = csv.writer(my_file)

        writer.writerow(header)
        for line in content:
            writer.writerow(line)

def main():
    print('going for main')
    try: 
        content = reader_csv(file_name)
        print('File successfully read')
        print('Content found: \n {}'.format(content[-1][0]))
    except: 
        print('Try fail going for exception')
        create_csv(file_name)
        print('File couldn\'t be read, a new file {} was created'.format(file_name))

main()