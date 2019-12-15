import os
import csv
import openpyxl
from pathlib import Path


class Converter:

    def __init__(self):
        os.chdir(os.path.expanduser('~/Downloads'))

    def discover_netflix_file(self):
        print("Looking for your Netflix history file...")
        for file in os.listdir('.'):
            if 'Netflix' in file and file.endswith('csv'):
                print("File Found! \n")
                return file

        print("Your Netflix history file could not be found in your downloads folder, program terminating")
        exit(1)


    def from_csv_to_workbook(self, new_file_name='NetflixHistory'):
        csv_file = self.discover_netflix_file()
        wb = openpyxl.Workbook()
        ws = wb.active

        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                ws.append(row)

            wb.save(new_file_name + '.xlsx')
            return '{}.xlsx'.format(new_file_name)
